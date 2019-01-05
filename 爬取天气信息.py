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

urls = ["http://lishi.tianqi.com/wuhan/201707.html",
        "http://lishi.tianqi.com/wuhan/201706.html",
        "http://lishi.tianqi.com/wuhan/201705.html"]
file = open('wuhan_weather.csv','w')
for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    weather_list = soup.select('div[class="tqtongji2"]')

    for weather in weather_list:
        weather_date = weather.select('a')[0].string.encode('utf-8')
        ul_list = weather.select('ul')
        i=0
        for ul in ul_list:
            li_list= ul.select('li')
            str=""
            for li in li_list:
                str += li.string.encode('utf-8').decode()+','
            if i!=0:
                file.write(str+'\n')
            i+=1
file.close()





url="http://lishi.tianqi.com/"
city_pinyin=pypinyin.slug('天津', style=0, separator=u'')
month='201705'
url_union=url+city_pinyin+'/'+month+'.html'

response = requests.get(url_union)
soup = BeautifulSoup(response.text, 'html.parser')
#weather_list = soup.select('div[class="tqtongji2"]')


weather=soup.find_all('div',attrs={'class':'tqtongji2'})[0]
weather_list=weather.find_all('ul')



w_city=[]
w_date=[]
w_high_temperature=[]
w_low_temperature=[]
w_weather=[]
w_wind_direction=[]
w_wind_power=[]
for i in range(1,len(weather_list)):
    w_city.append('天津')
    w_date.append(weather_list[i].find_all('a')[0].get_text().replace('-',''))
    w_high_temperature.append(weather_list[i].find_all('li')[1].get_text())
    w_low_temperature.append(weather_list[i].find_all('li')[2].get_text())
    w_weather.append(weather_list[i].find_all('li')[3].get_text())
    w_wind_direction.append(weather_list[i].find_all('li')[4].get_text())
    w_wind_power.append(weather_list[i].find_all('li')[5].get_text())

#合并至一张临时表中
temp_month_city_weather=pd.DataFrame({'w_city':w_city,'w_date':w_date,'high_temperature':w_high_temperature,'low_temperature':w_low_temperature,\
                                      'weather':w_weather,'wind_direction':w_wind_direction,'wind_power':w_wind_power})
