# 打开数据库连接
import pymysql as pymysql
import math

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

db = pymysql.connect(host='bj-cdb-cwu7v42u.sql.tencentcdb.com', port=62864, user='user', passwd='xmxc1234', db='test',
                     charset='utf8')  # charset='utf8'查询的有汉字此代码必须加上否则导出的是???
# 使用cursor（）方法获取操作游标
cursor = db.cursor()
# sql 查询语句
sql = "select id, client_name, latitude, longitude FROM t_client_elm limit 100"

# 执行sql语句
cursor.execute(sql)
# 获取所有记录列表
results = cursor.fetchall()

a = [["酒仙桥",116.687288, 40.2342],
     ["望京",116.462054, 39.914102],
     ["三里屯",116.442054, 39.954102]]
print(a.__len__())

for i in range(0, a.__len__()):
    i = 1  # 坐标定义
    name: str = a[i][0]
    lat2: float = a[i][1]
    lng2: float = a[i][2]
    i = i + 1
    for row in results:
        lat1=float(row[2])
        lng1=float(row[3])
        result = getDistan(lat1, lng1, lat2,lng2)
        if result <= 1:
            print(name + ":" + str(result))