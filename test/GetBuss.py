#!/usr/bin/python3
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

a = [["酒仙桥",116.687288, 40.2342],
     ["望京",116.462054, 39.914102],
     ["三里屯",116.442054, 39.954102]]
print(a.__len__())

for i in range(0, a.__len__()):
    name:str=a[i][0]
    lat1: float = a[i][1]
    lng1: float = a[i][2]
    i = i + 1
    result = getDistan(lat1, lng1, 116.6843, 40.2342)
    if result<=1:
        print(name+":"+str(result))


