# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(shenxianjun)s

#E_mail: shenxianjun.patrick@gmail.com

"""

from numpy import log1p
from sklearn.preprocessing import FunctionTransformer
from sklearn.datasets import load_iris

iris = load_iris()

#自定义转换函数为对数函数的数据变换
#第一个参数是单变元函数

aaa=FunctionTransformer(log1p).fit_transform(iris.data)


aaa=FunctionTransformer(np.log10).fit_transform(iris.data)

bbb=np.log10(iris.data)

aaa-bbb


import numpy as np

aaa=np.log10(1)




from sklearn.feature_selection import VarianceThreshold

#方差选择法，返回值为特征选择后的数据
#参数threshold为方差的阈值
ccc=VarianceThreshold(threshold=4).fit_transform(iris.data)

import pandas as pd

type(iris.data)
df=pd.DataFrame(iris.data,columns=iris.feature_names)

df.rename(index=str,columns={'sepal length (cm)':'sepal length', 'sepal width (cm)':'sepal width', 'petal length (cm)':'petal length',
       'petal width (cm)':'petal width'},inplace=True)


df.describe().variance

ccc=VarianceThreshold(threshold=0.25).fit_transform(df)

df.columns

type(iris)
iris.feature_nams.values()()

iris.feature_names










from sklearn.feature_selection import SelectKBest
from scipy.stats import pearsonr

#选择K个最好的特征，返回选择特征后的数据
#第一个参数为计算评估特征是否好的函数，该函数输入特征矩阵和目标向量，输出二元组（评分，P值）的数组，数组第i项为第i个特征的评分和P值。在此定义为计算相关系数
#参数k为选择的特征个数
SelectKBest(lambda X, Y: array(map(lambda x:pearsonr(x, Y), X.T)).T, k=2).fit_transform(iris.data, iris.target)








from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import GradientBoostingClassifier

#GBDT作为基模型的特征选择
ddd=SelectFromModel(GradientBoostingClassifier()).fit_transform(iris.data, iris.target)

