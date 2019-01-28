import calendar
import math

# print(dir(math))
# print("你好视界")
# for num in range(10,20):
#     for i in range(2,num):
#         if num%i==0:
#             j=num/i
#             print("%d=%d * %d" % (num,i,j))
#             break
#     else:print("这是一个质数")
# import time
#
# ticks=time.time()
# nowTime=time.localtime(ticks)
# localTime=time.asctime(nowTime)
# print(ticks)
# print(nowTime)
# print(localTime)
# print("----------------------------------")

#!/usr/bin/python
# -*- coding: UTF-8 -*-
sf=open("C:\\Users\\tl\\Desktop\\八爪鱼数据爬取\\name.txt","w")
# sf.write("小明")

name=sf.read(2)
print(name)
sf.close()
