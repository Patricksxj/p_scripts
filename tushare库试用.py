# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(shenxianjun)s

#E_mail: shenxianjun.patrick@gmail.com

"""

import pandas as pd
import numpy as np
import tushare as ts
import lxml


print(ts.__version__)


print(ts.get_cpi())

cpi_index=ts.get_cpi()

del cps_index

type(cpi_index)

cpi_index.info()

cpi_index[5:,"month"]


aaa=cpi_index[:5]

aaa=cpi_index[cpi_index['month']>'2015.1']

bbb=cpi_index[cpi_index['month']=='1990.1']['cpi']


a=aaa.shape[0]


range(aaa.shape[0])

ccc=np.asarray(aaa.iloc[:,1].astype(float))-np.asarray(bbb.astype(float))



for i in range(aaa.shape[0]):
    print(aaa.iloc[i,1])
    print("aaa result={result}".format(result=aaa[i,1]))

df=pd.DataFrame(columns=['month','cpi'])
for i in range(aaa.shape[0]):
    gap=pd.DataFrame({"month":aaa.iloc[i,0],"cpi":(aaa.iloc[i,1].astype(float)-bbb.astype(float))})
    df=df.append(gap)



#票房数据
piaofang=ts.day_cinema('2017-10-02')

pd.set_option

pd.set_option('display.max_columns', 200)
pd.set_option('display.width', 1000)


piaofang[piaofang['price'].max()]

rl_piaofang=ts.realtime_boxoffice()

last_m_pf=ts.month_boxoffice('2017-07')

piaofang_df=pd.DataFrame()


