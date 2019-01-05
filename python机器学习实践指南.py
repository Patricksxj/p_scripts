# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(shenxianjun)s

#E_mail: shenxianjun.patrick@gmail.com

"""

import os
import pandas as pd
import requests


PATH = r'C:\Users\Administrator\Desktop'

r = requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')


with open(PATH + '\iris.csv', 'w') as f:
    f.write(r.text)
    f.close()

df=pd.read_csv(PATH +'\iris.csv',names=['sepal_length' ,'sepal_width','petal_length' ,'petal_width','class'])


df.head()

#前两行
df.ix[:1,:]

#特定条件：
'''
字段sepal length==4.8时的所有数据
'''

df.ix[df.ix[:,'sepal_length']==4.8,:]


'''
字段petal length>2时,产出sepal length,petal length
'''
df.ix[df.ix[:,'petal_length']>=2,['sepal_length','petal_length']]


df.head()

df.index

df.describe()

#:3含义是保留前三行，3：意思是去掉前三行保留剩余部分
df.ix[:3,[x for x in df.columns if 'width' in x]]

df['class'].count()

bbb=df[-(df['class']=='Iris-virginica')]

df.query('sepal_length > 5')

#分类求频数
bbb.groupby('class').count()
df.groupby('class')['class'].count()

#分类求和

df.groupby('class').agg({'sepal_length':np.max,'sepal_width':np.sum})


df.groupby('class').size()

#等同于distinct

df.groupby('class').agg({'sepal_length':pd.Series.nunique})#去除重复

df.groupby('class').agg({'sepal_length':pd.Series.count})

df.nlargest(5,columns=['sepal_length'])



import seaborn as sns
sns.pairplot(df,hue="class")

df.groupby('class')['class'].count()

df['class2']=df['class'].map({'Iris-setosa':'IS','Iris-versicolor':'IV','Iris-virginica':'IG'})



df['class3']=df['class'].apply(lambda x: 'y' if 'setosa' in x else 'n')

df.groupby('class2')['class2'].count()

df.groupby('class3')['class3'].count()


import statsmodels.api as sm







