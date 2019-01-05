# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(shenxianjun)s

#E_mail: shenxianjun.patrick@gmail.com

"""

path=r"G:\统计类知识与材料\数据集\手机号段-201810-415311\phone-qqzeng-201810-415311.xlsx"



import pandas as pd
phone_data=pd.ExcelFile(path)

phone_data.head()



df = phone_data.parse('号段数据库',skiprows=[0],names=['prefix',	'phone','province',	'city',	'isp',	'post_code','city_code','area_code'])

type(df)

df.head()

df[df['phone']==1999580]



import time
from sqlalchemy import create_engine
import pandas as pd

engine= create_engine('postgresql+psycopg2://postgres:sxj168109921@localhost:5432/postgres')
try:
    df.to_sql('phone_2_city', engine, if_exists='append', index=False,chunksize=1000)
except Exception as e:
    print(e)