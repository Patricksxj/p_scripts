# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(shenxianjun)s

#E_mail: shenxianjun.patrick@gmail.com

"""


import requests
from bs4 import BeautifulSoup
import pandas as pd
import pypinyin


import time
from sqlalchemy import create_engine
import psycopg2




#1）从数据库中导出临时存放的数据



#数据导出至pandas

engine = create_engine('postgresql+psycopg2://postgres:sxj168109921@localhost:5432/mydb')


begin=time.clock()
tempdata_union = pd.read_sql_query('select * from "temp_data_union"',con=engine)
end=time.clock()

print("The function run time is : %.03f seconds" %(end-begin))



#2）产出同一城市不同月份的名单

temp_data_for_weather=tempdata_union[['year','month','qry_city']]

temp_data_for_weather=temp_data_for_weather.drop_duplicates(['year','month','qry_city'],'first')

#temp_data_for_weather.reindex(range(len(temp_data_for_weather)),copy=True)



temp_data_for_weather['city_nick_name']=''
for i in temp_data_for_weather.index:
    if '蒙古族藏族自治州' in temp_data_for_weather['qry_city'][i]:
        temp_data_for_weather['city_nick_name'][i]=temp_data_for_weather['qry_city'][i].replace('蒙古族藏族自治州','')
    elif '布依族苗族自治州' in temp_data_for_weather['qry_city'][i]:
        temp_data_for_weather['city_nick_name'][i]=temp_data_for_weather['qry_city'][i].replace('布依族苗族自治州','')
    elif temp_data_for_weather['qry_city'][i]=='巴音郭楞蒙古自治州':
        temp_data_for_weather['city_nick_name'][i]='巴州'
    elif temp_data_for_weather['qry_city'][i]=='海南藏族自治州':
        temp_data_for_weather['city_nick_name'][i]='海南州'
    elif '地区' in temp_data_for_weather['qry_city'][i]:
        temp_data_for_weather['city_nick_name'][i]=temp_data_for_weather['qry_city'][i].replace('地区','')
    elif '盟' in temp_data_for_weather['qry_city'][i]:
        temp_data_for_weather['city_nick_name'][i]=temp_data_for_weather['qry_city'][i].replace('盟','')
    elif '市' in temp_data_for_weather['qry_city'][i]:
        temp_data_for_weather['city_nick_name'][i]=temp_data_for_weather['qry_city'][i].replace('市','')
    else:
        temp_data_for_weather['city_nick_name'][i]=temp_data_for_weather['qry_city'][i]



def scrapy_weather(city_nick_name='天津',month='201705',city_real_name='天津市'):
    url="http://lishi.tianqi.com/"
    city_pinyin=pypinyin.slug(city_nick_name, style=0, separator=u'')
    url_union=url+city_pinyin+'/'+month+'.html'
    response = requests.get(url_union)
    soup = BeautifulSoup(response.text, 'html.parser')
    w_city=[]
    w_date=[]
    w_high_temperature=[]
    w_low_temperature=[]
    w_weather=[]
    w_wind_direction=[]
    w_wind_power=[]
    w_parse_status=[]
    try:
        weather=soup.find_all('div',attrs={'class':'tqtongji2'})[0]
        weather_list=weather.find_all('ul')
        for i in range(1,len(weather_list)):
            w_city.append(city_real_name)
            w_date.append(weather_list[i].find_all('a')[0].get_text().replace('-',''))
            w_high_temperature.append(weather_list[i].find_all('li')[1].get_text())
            w_low_temperature.append(weather_list[i].find_all('li')[2].get_text())
            w_weather.append(weather_list[i].find_all('li')[3].get_text())
            w_wind_direction.append(weather_list[i].find_all('li')[4].get_text())
            w_wind_power.append(weather_list[i].find_all('li')[5].get_text())
            w_parse_status.append('1')
    #合并至一张临时表中
        temp_month_city_weather=pd.DataFrame({'w_parse_status':w_parse_status,'w_city':w_city,'w_date':w_date,'high_temperature':w_high_temperature,'low_temperature':w_low_temperature,\
                                      'weather':w_weather,'wind_direction':w_wind_direction,'wind_power':w_wind_power})
    except :
        w_parse_status.append('0')
        w_city.append(city_nick_name)
        w_date.append(month)
        w_high_temperature.append('')
        w_low_temperature.append('')
        w_weather.append('')
        w_wind_direction.append('')
        w_wind_power.append('')
        temp_month_city_weather=pd.DataFrame({'w_parse_status':w_parse_status,'w_city':w_city,'w_date':w_date,'high_temperature':w_high_temperature,'low_temperature':w_low_temperature,\
                                      'weather':w_weather,'wind_direction':w_wind_direction,'wind_power':w_wind_power})
    return temp_month_city_weather


w_city=[]
w_date=[]
w_high_temperature=[]
w_low_temperature=[]
w_weather=[]
w_wind_direction=[]
w_wind_power=[]
w_parse_status=[]
#初始化空表
month_city_weather=pd.DataFrame({'w_parse_status':w_parse_status,'w_city':w_city,'w_date':w_date,'high_temperature':w_high_temperature,'low_temperature':w_low_temperature,\
                                      'weather':w_weather,'wind_direction':w_wind_direction,'wind_power':w_wind_power})

#获取全部地址各月份的天气情况
for i in  temp_data_for_weather.index:
    temp_month_city_weather=scrapy_weather(city_nick_name=temp_data_for_weather['city_nick_name'][i]\
                                             ,month=temp_data_for_weather['year'][i]+temp_data_for_weather['month'][i],city_real_name=temp_data_for_weather['qry_city'][i])
    month_city_weather=month_city_weather.append(temp_month_city_weather,ignore_index=True)


#查看多少城市爬取异常的
month_city_weather[month_city_weather['w_parse_status']=='0']






#查回信息保存至数据库
begin=time.clock()
engine = create_engine('postgresql+psycopg2://postgres:sxj168109921@localhost:5432/mydb')
month_city_weather.to_sql('month_city_weather', engine)
end=time.clock()


del tempdata_union['year_month']

#关联天气与之前明细数据
tempdata_union['year_month_day']=tempdata_union['year']+tempdata_union['month']+tempdata_union['day']

tempdata_union_add_w=pd.merge(tempdata_union,month_city_weather,how='left',left_on=['year_month_day','qry_city'],right_on=['w_date','w_city'])


#查询解析异常城市
tempdata_union_add_w[tempdata_union_add_w['w_parse_status']!='1']['qry_city'].value_counts()

#对解析异常城市将w_parse_status标注为0

tempdata_union_add_w.loc[tempdata_union_add_w['w_parse_status']!='1','w_parse_status']='0'

#验证数据ok
tempdata_union_add_w[tempdata_union_add_w['w_parse_status']!='1']['w_parse_status'].value_counts()




#查回信息保存至数据库：基础信息+城市解析+天气解析
begin=time.clock()
engine = create_engine('postgresql+psycopg2://postgres:sxj168109921@localhost:5432/mydb')
tempdata_union_add_w.to_sql('tempdata_union_add_w', engine)
end=time.clock()