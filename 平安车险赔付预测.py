# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(shenxianjun)s

#E_mail: shenxianjun.patrick@gmail.com

"""

import pandas as pd
import os
import datetime
import time
import numpy as np
import random

working_path=os.getcwd()
path_train = working_path+'/data/dm/train.csv'

def pd_read_csv():
    """
    文件读取模块，头文件见columns.
    :return:
    """
    # for filename in os.listdir(path_train):
    tempdata = pd.read_csv(path_train)
    tempdata.columns = ["TERMINALNO", "TIME", "TRIP_ID", "LONGITUDE", "LATITUDE", "DIRECTION", "HEIGHT", "SPEED",
                        "CALLSTATE", "Y"]
    return tempdata


tempdata=pd_read_csv()



#

'''
1.特征工程
1.1 对时间字段做解析：拆分为，年份，星期几，月份，季节，上午/下午，小时 √
1.2 对经纬度，解析为城市 √
1.3 尝试判断当时的天气，通过获取地址与时间
1.4 将海拔做分段处理，统计不同海拔高度与赔付率的线性关系
1.5 将速度做分段处理，统计不同速度与赔付率的线性关系


赔付率概念介绍
赔付率=赔款/保费
#https://wenku.baidu.com/view/852b30e3710abb68a98271fe910ef12d2af9a918.html

'''

datetime.datetime.utcfromtimestamp(tempdata['TIME'][0]).strftime('%Y-%m-%d %H:%M:%S')

datetime.datetime.utcfromtimestamp(tempdata['TIME'][1]).strftime('%Y-%m-%d %H:%M:%S')



utc_datetime=[]
year=[]
month=[]
day=[]
hour=[]
weekday=[]
am_pm=[]
for i in range(len(tempdata)):
    try:
        utc_datetime.append(datetime.datetime.utcfromtimestamp(tempdata['TIME'][i]).strftime('%Y-%m-%d %H:%M:%S'))
        year.append(datetime.datetime.utcfromtimestamp(tempdata['TIME'][i]).strftime('%Y'))
        month.append(datetime.datetime.utcfromtimestamp(tempdata['TIME'][i]).strftime('%m'))
        day.append(datetime.datetime.utcfromtimestamp(tempdata['TIME'][i]).strftime('%d'))
        hour.append(datetime.datetime.utcfromtimestamp(tempdata['TIME'][i]).strftime('%H'))
        weekday.append(datetime.datetime.utcfromtimestamp(tempdata['TIME'][i]).strftime('%A'))
        am_pm.append(datetime.datetime.utcfromtimestamp(tempdata['TIME'][i]).strftime('%p'))
    except IndexError:
        pass


tempdata2=pd.DataFrame({'utc_datetime':utc_datetime,'year':year,'month':month,'day':day,'hour':hour\
                        ,'weekday':weekday,'am_pm':am_pm})

tempdata3=pd.concat((tempdata,tempdata2),axis=1)

#
#由于百度api的限制，尚未认证的情况下一天只能解析6000次，
#对每个人，每次trip随机采集一个gps，用于后续解析

#统计测试集中有多少人
max_terminalno=np.max(tempdata['TERMINALNO'])

#每人有多少次trip
trip_list=tempdata['TRIP_ID'].groupby(tempdata['TERMINALNO']).max()

#每次trip的统计次数

#one_trip_list_cnt=tempdata['TRIP_ID'].groupby([tempdata['TERMINALNO'],tempdata['TRIP_ID']]).count()



#随机取每一个人每一次trip的经纬度

need_query_id=[]
need_query_trip=[]
need_query_long=[]
need_query_lat=[]
for i in range(1,max_terminalno+1):
    for j in range(1,trip_list[i]+1):
        one_trip_list=tempdata[(tempdata['TERMINALNO']==i) & (tempdata['TRIP_ID']==j)]
        rand_num=random.choice(one_trip_list.index.values)
        temp_long=one_trip_list['LONGITUDE'][rand_num]
        temp_lat=one_trip_list['LATITUDE'][rand_num]
        temp_terminalno=one_trip_list['TERMINALNO'][rand_num]
        temp_trip_id=one_trip_list['TRIP_ID'][rand_num]
        need_query_id.append(temp_terminalno)
        need_query_trip.append(temp_trip_id)
        need_query_long.append(temp_long)
        need_query_lat.append(temp_lat)

#合并临时表

temp_need_qry_df=pd.DataFrame({'need_query_id':need_query_id,'need_query_trip':need_query_trip,
                               'need_query_long':need_query_long,'need_query_lat':need_query_lat})




import json
from urllib.request import urlopen, quote
import requests,csv
import urllib
import pandas as pd


#建立gps解析经纬度函数
def getaddress(location_long,location_lat):
    url = 'http://api.map.baidu.com/geocoder/v2/'
    rest='callback=renderReverse&location='
    output = 'json'
    ak = '6ZSttxRyyIqGl6mtCOFRtifvLtuliNr9'
    uri = url + '?' + rest + str(location_lat) + ',' + str(location_long) + '&output=' + output +'&pois=0&extensions_poi=null' + '&ak=' + ak
    req = urlopen(uri)
    res = req.read().decode() #将其他编码的字符串解码成unicode
    res_clean=str.replace(res,'renderReverse&&renderReverse(','')#剔除无效字符，转换为json
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


qry_status=[]
qry_country=[]
qry_province=[]
qry_city=[]
qry_district=[]
qry_city_level=[]
qry_formatted_address=[]


for i in range(len(temp_need_qry_df)):
    tmp_status,tmp_country,tmp_province,tmp_city,tmp_district,\
    tmp_city_level,tmp_formatted_address=getaddress(temp_need_qry_df['need_query_long'][i],temp_need_qry_df['need_query_lat'][i])
    qry_status.append(tmp_status)
    qry_country.append(tmp_country)
    qry_province.append(tmp_province)
    qry_city.append(tmp_city)
    qry_district.append(tmp_district)
    qry_city_level.append(tmp_city_level)
    qry_formatted_address.append(tmp_formatted_address)




temp_need_qry_df2=pd.DataFrame({'need_query_id':need_query_id,'need_query_trip':need_query_trip,
                               'need_query_long':need_query_long,'need_query_lat':need_query_lat,
                               'qry_status':qry_status,'qry_country':qry_country,'qry_province':qry_province,
                               'qry_city':qry_city,'qry_district':qry_district,'qry_city_level':qry_city_level,
                               'qry_formatted_address':qry_formatted_address})





#关联结果表


tempdata_union = pd.merge(tempdata3, temp_need_qry_df2,how='left',left_on=['TERMINALNO','TRIP_ID'],right_on=['need_query_id','need_query_trip'])


tempdata3.to_csv('raw_data.csv')

temp_need_qry_df2.to_csv('baidu_parse_city.csv')

tempdata_union.to_csv('tempdata_union.csv')

import time
from sqlalchemy import create_engine
import psycopg2

#pandas导入数据库

#原数据加工后的结果导入库，防止后续再次从百度取数
begin=time.clock()
engine = create_engine('postgresql+psycopg2://postgres:sxj168109921@localhost:5432/mydb')
tempdata3.to_sql('raw_data_add', engine)
end=time.clock()


#百度地址解析后结果导入库
begin=time.clock()
engine = create_engine('postgresql+psycopg2://postgres:sxj168109921@localhost:5432/mydb')
temp_need_qry_df2.to_sql('baidu_parse_city', engine)
end=time.clock()

#合并后表导入数据库
begin=time.clock()
engine = create_engine('postgresql+psycopg2://postgres:sxj168109921@localhost:5432/mydb')
tempdata_union.to_sql('temp_data_union', engine)
end=time.clock()


tempdata_union['qry_city'].groupby(tempdata_union['qry_city']).count()




