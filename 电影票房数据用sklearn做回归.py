# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(shenxianjun)s

#E_mail: shenxianjun.patrick@gmail.com

"""

import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import cross_val_predict
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

t_movie=pd.read_table('D:\\P_WORKPLACE\\movie.csv',sep=',',index_col=['movie_name'],encoding='gbk')


#1)提取需要的变量
t_movie2=t_movie.loc[:,['boxoffice','Broadcast_times','watched_people',
'runtime','reality','remake','sequel','director_year','direct_n_movies',
'award','director_change','baidu_index1','baidu_index2']]


t_movie2.shape

x,y=t_movie2.iloc[:,1:13],t_movie2.iloc[:,0]

x_array=np.array(x.loc[:,:])

np.isnan(x_array)

imput=preprocessing.Imputer(strategy='mean',missing_values='NaN',axis=0)

imput.fit(x_array)


x_array=imput.fit_transform(x_array)

#将空值填补为票平均值
x.loc[:,:]=x_array




#对x变量做标准化处理
'''
1)先将x变量准换为数组
2）标准化处理
'''
x_array2=x_array
x_std=preprocessing.StandardScaler()
x_std.fit(x_array2[:,:12])
x_array3=x_std.transform(x_array2[:,:12])


#将标准化后的结果赋值给x

x_train=x_array3
y_train=np.array(y)



# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(x_train,y_train)

# Make predictions using the testing set
y_pre = regr.predict(x_train)

# The coefficients
coef_list=regr.coef_


var_array=np.array(['Broadcast_times','watched_people',
'runtime','reality','remake','sequel','director_year','direct_n_movies',
'award','director_change','baidu_index1','baidu_index2'])



aaa=np.column_stack((var_array,coef_list))

aaa=var_array.col


print('Coefficients: \n', regr.coef_)
# The mean squared error
print("Mean squared error: %.2f"
      % mean_squared_error(y_train, y_pre))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(y_train, y_pre))



