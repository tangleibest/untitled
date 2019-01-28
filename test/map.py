import pymysql
import math
#import numpy as np
#import pandas as pd
from pandas import Series, DataFrame


# 打开数据库连接
db = pymysql.connect(host='bj-cdb-cwu7v42u.sql.tencentcdb.com',port=62864,user='user',passwd='xmxc1234',db='mapmarktest',charset='utf8')# charset='utf8'查询的有汉字此代码必须加上否则导出的是???
# 使用cursor（）方法获取操作游标
cursor = db.cursor()
# sql 查询语句

sql = "SELECT \
	doc_id,\
	shop_id,\
	client_name,\
	address,\
	latitude,\
	longitude,\
	month_sale_num,\
	update_count,\
	float_delivery_fee,\
	first_cate,\
	'elm' platform \
FROM\
	t_map_client_elm_beijing_mark"

# 执行sql语句
cursor.execute(sql)
# 获取所有记录列表
results = cursor.fetchall()
print(len(results[1]))

cursor.close()  # 关闭游标
db.close()  # 关闭连接

EARTH_REDIUS = 6378.137
pi = 3.1415926
def rad(d):
    return d * pi / 180.0

def getDistan(lat1, lng1, lat2, lng2):
    radLat1 = rad(lat1)
    radLat2 = rad(lat2)
    a = radLat1 - radLat2
    b = rad(lng1) - rad(lng2)
    s = 2 * math.asin(math.sqrt(math.pow(math.sin(a / 2), 2) + math.cos(radLat1) * math.cos(radLat2) * math.pow(
        math.sin(b / 2), 2)))
    s = s * EARTH_REDIUS
    return s

a = [["百脑汇",39.92406,116.445756],
     ["方庄",39.868324,116.447676],
     ["四道口",39.961826,116.338341],
     ["驼房营",39.970994,116.502621],
     ["悠乐汇",39.989391,116.477081],
     ["西直门",39.95302,116.35335]]

print(len(a))
dis = []

for j in range(len(a)):
    point = str(a[j][0])
    lat1 = float(a[j][1])
    lng1 = float(a[j][2])
    for i in range(len(results)):
        doc_id = int(results[i][0])
        shop_id = str(results[i][1])
        client_name = str(results[i][2])
        address = str(results[i][3])
        lat2 = float(results[i][4])
        lng2 = float(results[i][5])
        month_sale_num = float(results[i][6])
        update_count = int(results[i][7])
        average_price = str(results[i][8])
        cate_name = str(results[i][9])
        platform = str(results[i][10])
        result = getDistan(lat1, lng1, lat2, lng2)
        i = i + 1
        if result <= 3:
            dis.append([point, result, doc_id, shop_id, client_name, month_sale_num, update_count, average_price, cate_name, platform, address])

print(dis)


'''for i in range(len(dis)):
    sql = "insert into t_beijing_shangquan_cal2(id, shangquan, distance, client_name, month_sale_num, cate, platform) values('{}','{}','{}','{}','{}','{}','{}')"\
        .format(pymysql.escape_string(str(dis[i][0])),pymysql.escape_string(str(dis[i][1])),pymysql.escape_string(str(dis[i][2])),
                pymysql.escape_string(str(dis[i][3])),pymysql.escape_string(str(dis[i][4])),pymysql.escape_string(str(dis[i][5])),
                pymysql.escape_string(str(dis[i][6])))
    print(sql)
    cursor.execute(sql)
    db.commit()'''



frame = DataFrame(dis,columns=[point, result, doc_id, shop_id, client_name, month_sale_num, update_count, average_price, cate_name, platform,address])
#print(frame.groupby('point')['month_sale_num'].sum().sort_values(ascending=False))
frame.to_excel('D:\\zgf_elm.xlsx')