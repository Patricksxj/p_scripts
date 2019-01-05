# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(shenxianjun)s

#E_mail: shenxianjun.patrick@gmail.com

"""

#观察数据分布情况

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

import time
from sqlalchemy import create_engine
import psycopg2
from sklearn.preprocessing import StandardScaler


begin=time.clock()
engine = create_engine('postgresql+psycopg2://postgres:sxj168109921@localhost:5432/mydb')
tempdata_union_add_w = pd.read_sql_query('select * from "tempdata_union_add_w"',con=engine)
end=time.clock()
print("The function run time is : %.03f seconds" %(end-begin))




#产出建模中间数据集，对每一个人，同一次trip_id取平均一条记录


tempdata_union_sample1=tempdata_union_add_w.groupby(['TERMINALNO','TRIP_ID'],as_index=False).agg({'DIRECTION': np.mean,'HEIGHT': np.mean,'SPEED': np.median,\
                                                  'CALLSTATE': np.max,'Y': np.max})


len(tempdata_union_sample1['TERMINALNO'])

aaa=tempdata_union_sample1.groupby(['TERMINALNO','TRIP_ID'],as_index=False).TERMINALNO.nunique()


tempdata_union_sample2=tempdata_union_add_w.drop_duplicates(['TERMINALNO','TRIP_ID','weekday','qry_status','qry_country','qry_province','qry_city','qry_district','weather','wind_direction','wind_power'
'am_pm','year','month','day','high_temperature','low_temperature'],keep='first')

tempdata_union_sample3=tempdata_union_sample2.drop_duplicates(['TERMINALNO','TRIP_ID'],keep='first')

tempdata_union_sample3=tempdata_union_sample3[['TERMINALNO','TRIP_ID','weekday','qry_status','qry_country','qry_province','qry_city','qry_district','weather','wind_direction','wind_power',
'am_pm','year','month','day','high_temperature','low_temperature']]



len(tempdata_union_sample3['TERMINALNO'])



#合并样本数据

tempdata_union_sample4=pd.merge(tempdata_union_sample1,tempdata_union_sample3,how='left',left_on=['TERMINALNO','TRIP_ID'],right_on=['TERMINALNO','TRIP_ID'])





weather_dict={'晴':1,np.nan:1,
'多云':2,'多云转阴':2,'阴':2,'阴~多云':2,
'雷阵雨~多云':3,'雷阵雨转多云':3,'霾':3,'雾':3,'阵雨~多云':3,'阵雨~阴':3,
'雷阵雨':4,'小雪':4,'小雨':4,'雨夹雪':4,'阵雪':4,'阵雨':4,'中雨转小雨':4,'中雨转多云':4,
'多云转中雨':5,'小到中雪':5,'小到中雨':5,'小雨转中雨':5,'中雪':5,'中雨':5,'中雨~阵雨':5,
'大雨':6,'中到大雨':6,
'暴雨':7,'大到暴雨':7}



#更新至主表
tempdata_union_sample4['weather_label'] = tempdata_union_sample4['weather'].map(weather_dict)


wind_power_dict={np.nan:1,'1级':1,'微风':1,
'2级':2,'小于3级':2,
'3-4级':3,'3-4级转小于3级':3,'3级':3,'小于3级转3-4级':3,
'4级':4,
'5级':5}

#更新至主表
tempdata_union_sample4['wind_power_label'] = tempdata_union_sample4['wind_power'].map(wind_power_dict)


tempdata_union_sample4[['high_temperature','low_temperature']]=tempdata_union_sample4[['high_temperature','low_temperature']].astype(float)


#对缺失值填充

num_variable=['DIRECTION','HEIGHT','SPEED','high_temperature','low_temperature']
for i in num_variable:
    tempdata_union_sample4[i].fillna(tempdata_union_sample4[i].mean())


#对未解析出的填整体温度

tempdata_union_sample4.loc[tempdata_union_sample4['high_temperature'].isnull(),'high_temperature']=tempdata_union_sample4['high_temperature'].mean()
tempdata_union_sample4.loc[tempdata_union_sample4['low_temperature'].isnull(),'low_temperature']=tempdata_union_sample4['low_temperature'].mean()





#将样本数据保存至数据库
begin=time.clock()
engine = create_engine('postgresql+psycopg2://postgres:sxj168109921@localhost:5432/mydb')
tempdata_union_sample4.to_sql('tempdata_union_sample4', engine)
end=time.clock()





#对字符型变量进行哑变量处理
#选出需要做哑变量的变量
char_variable=['qry_province','qry_city','am_pm','month','day','weekday','weather_label','wind_power_label','CALLSTATE']

tempdata_union_dummies=pd.get_dummies(tempdata_union_sample4[char_variable])

char_variable_dummies=list(tempdata_union_dummies.columns.values)


#对数值型变量做标准化操作

num_variable=['DIRECTION','HEIGHT','SPEED','high_temperature','low_temperature']


tempdata_union_scaled=tempdata_union_sample4[num_variable].apply(lambda x:(x-np.mean(x))/(np.max(x)-np.min(x)))




#合并至最终表
tempdata_union_final=pd.concat([tempdata_union_sample4[['TERMINALNO','TRIP_ID']],\
                                tempdata_union_dummies,tempdata_union_scaled],axis=1,ignore_index=True)





begin=time.clock()
engine = create_engine('postgresql+psycopg2://postgres:sxj168109921@localhost:5432/mydb')
tempdata_union_dummies.to_sql('tempdata_union_dummies', engine)
end=time.clock()

print("The function run time is : %.03f seconds" %(end-begin))


begin=time.clock()
engine = create_engine('postgresql+psycopg2://postgres:sxj168109921@localhost:5432/mydb')
tempdata_union_scaled.to_sql('tempdata_union_scaled', engine)
end=time.clock()

print("The function run time is : %.03f seconds" %(end-begin))



begin=time.clock()
engine = create_engine('postgresql+psycopg2://postgres:sxj168109921@localhost:5432/mydb')
tempdata_union_final.to_sql('tempdata_union_final', engine)
end=time.clock()

print("The function run time is : %.03f seconds" %(end-begin))














#产出测试集与训练集
from sklearn.model_selection import train_test_split
from sklearn.ensemble import BaggingRegressor
from sklearn.model_selection import cross_val_score


X_train,X_test,y_train,y_test=train_test_split(tempdata_union_final,tempdata_union_sample4['Y'],test_size=0.25,random_state =0)


type(X_train)


#开始建立模型
from sklearn.linear_model import Ridge


alphas = np.logspace(-3,2,50)
test_scores = []
ridge_test_dict={}
for alpha in alphas:
    clf = Ridge(alpha)
    test_score = np.sqrt(-cross_val_score(clf, X_train, y_train, cv=10, scoring='neg_mean_squared_error'))
    test_scores.append(np.mean(test_score))
    ridge_test_dict[alpha]=np.mean(test_score)





plt.plot(alphas,test_scores)
#plt.axis([-1, 5, 0, 1])
plt.show()


ridge_result=min(ridge_test_dict.items(), key=lambda x: x[1])
print(ridge_result)
#(5.9636233165946431, 0.13507346978306825)







ridge = Ridge(0.13894954943731375)

params = [1,2,5,7,8,9, 10,12,13, 15,17,19, 20, 25, 30, 40]
test_scores = []
bagging_test_dict={}
for param in params:
    clf = BaggingRegressor(n_estimators=param, base_estimator=ridge)
    test_score = np.sqrt(-cross_val_score(clf, X_train, y_train, cv=20, scoring='neg_mean_squared_error'))
    test_scores.append(np.mean(test_score))
    bagging_test_dict[param]=np.mean(test_score)


plt.plot(params,test_scores)
#plt.axis([-1, 5, 0, 1])
plt.show()


bagging_result=min(bagging_test_dict.items(), key=lambda x: x[1])
print(bagging_result)
#(13, 0.6477439379557408)







"""
        查看数据集
"""
print('\n===================== 数据查看 =====================')
print('训练集有{}条记录。'.format(len(tempdata_union)))


# 可视化各类别的数量统计图
temp=tempdata_union[tempdata_union['Y']!=0]['Y'].astype(float)



tempdata_union['Y'].value_counts().plot.bar()


#平均速度
tempdata_union['SPEED'].plot.hist()


tempdata_union['DIRECTION'].plot.hist()


tempdata_union['HEIGHT'].plot.hist()


tempdata_union['CALLSTATE'].plot.hist()



insurance_rate=pd.DataFrame({'insurance':temp,'insurance_log1p':np.log1p(temp)})


insurance_rate.hist()
