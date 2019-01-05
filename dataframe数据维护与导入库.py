# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 13:36:35 2017

@author: Administrator
"""

import pandas as pd
import numpy as np


df = pd.read_csv('E:\\party_info.txt',names=['id','name','sex','nation','jg','dzz','idcard','address','mobile','telephone','education'], sep=',', header=None, dtype=str, na_filter=False,error_bad_lines =False)

df.describe()



df[df.columns] = df.apply(lambda x: x.str.replace("INSERT INTO party_table VALUES \(",''))

df[df.columns] = df.apply(lambda x: x.str.strip())

df[df.columns] = df.apply(lambda x: x.str.replace("\);",''))

df[df.columns] = df.apply(lambda x: x.str.replace("'",''))



import time
from sqlalchemy import create_engine
import psycopg2

#导入数据

begin=time.clock()
engine = create_engine('postgresql+psycopg2://postgres:sxj168109921@localhost:5432/mydb')
df.to_sql('party_info', engine)
end=time.clock()

print("The function run time is : %.03f seconds" %(end-begin))



del df




begin=time.clock()
import psycopg2
conn = psycopg2.connect(database="mydb", user="postgres", password="sxj168109921", host="127.0.0.1", port="5432")

#开始查询
cur = conn.cursor()
sql = "select count(*) from party_info"
cur.execute(sql)
rows=cur.fetchall()
print ("all=",rows[0])
conn.commit() # 查询时无需，此方法提交当前事务。如果不调用这个方法，无论做了什么修改，自从上次调用#commit()是不可见的
conn.close()

end=time.clock()

print("The function run time is : %.03f seconds" %(end-begin))



#数据导出至pandas
begin=time.clock()
df = pd.read_sql_query('select * from "party_info"',con=engine)
end=time.clock()
print("The function run time is : %.03f seconds" %(end-begin))

df.head()
del df2


df2=df[df['name']=='曹晓东']







#数据导出至pandas
begin=time.clock()
df2 = pd.read_sql_query("select * from party_info where dzz like %上缝居民区%第二党支部%",con=engine)
end=time.clock()
print("The function run time is : %.03f seconds" %(end-begin))

df.shape



df.query('name==["裘国琴","颜友莉"]')






