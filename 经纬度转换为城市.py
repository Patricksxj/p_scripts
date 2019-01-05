# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(shenxianjun)s

#E_mail: shenxianjun.patrick@gmail.com

"""

loc_cache = {}
key = '6ZSttxRyyIqGl6mtCOFRtifvLtuliNr9'


import json
from urllib.request import urlopen, quote
import requests,csv
import urllib
import pandas as pd #导入这些库后边都要用到

def getaddress(location_long,location_lat):
    url = 'http://api.map.baidu.com/geocoder/v2/'
    rest='callback=renderReverse&location='
    output = 'json'
    ak = '6ZSttxRyyIqGl6mtCOFRtifvLtuliNr9'
    uri = url + '?' + rest + str(location_lat) + ',' + str(location_long) + '&output=' + output +'&pois=0&extensions_poi=null' + '&ak=' + ak
    req = urlopen(uri)
    res = req.read().decode() #将其他编码的字符串解码成unicode
    res_clean=str.replace(res,'renderReverse&&renderReverse(','')
    length=len(res_clean)
    res_clean_part = res_clean[0:length-1]
    temp = json.loads(res_clean_part) #对json数据进行解析
    country=temp['result']['addressComponent']['country']
    province=temp['result']['addressComponent']['province']
    city=temp['result']['addressComponent']['city']
    status=temp['status']
    district=temp['result']['addressComponent']['district']
    city_level=temp['result']['addressComponent']['city_level']
    formatted_address=temp['result']['formatted_address']
    return status,country,province,city,district,city_level,formatted_address


status,country,province,city,city_level,formatted_address=getaddress(112.956352,28.136091)

print('status:',status)
print('country:',country)
print('province:',province)
print('city:',city)
print('city_level:',city_level)
print('formatted_address:',formatted_address)

http://api.map.baidu.com/geocoder/v2/?callback=renderReverse&location=35.658651,139.745415&output=json&pois=1&ak=您的ak //GET请求