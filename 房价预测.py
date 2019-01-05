# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(shenxianjun)s

#E_mail: shenxianjun.patrick@gmail.com

"""

import pandas as pd
import numpy as np
from matplotlib import  pyplot as plt


house_price_train=pd.read_csv('house_price_train.csv',header=0,index_col='Id')

house_price_test=pd.read_csv('house_price_test.csv',header=0,index_col='Id')


"""
主要任务：
0.合并数据集  √

1.空值处理：
1）对于数值型空值填充  √
2）对字符型NA填评述最大值 √

2.数据标准化
1）自变量数据标准化
2）因变量数据做平滑处理  √
3）字符型变量做哑变量
"""

#1.观察因变量--房价的分布


plt.bar(house_price_train.index,house_price_train.SalePrice)


prices=pd.DataFrame({'price':house_price_train.SalePrice,'log1p':np.log1p(house_price_train.SalePrice)})


prices.hist()



house_price_train.index.min()

house_price_train.index.max()

#test_datasets index num from 1461

house_price_test.index.min()

house_price_test.index.max()


y=np.log1p(house_price_train.pop('SalePrice'))

house_price_train.SalePrice.count()

#合并数据集
x=pd.concat([house_price_train,house_price_test],axis=0)

#字符型变量
x_ojects=x.columns[x.dtypes=='object']

#数值型变量
x_num_ojects=x.columns[x.dtypes!='object']



#观察是否都是数值型

for i in range(len(x_num_ojects)):
    print("var_name:%s,var_values:%s" %(x_num_ojects[i],x[x_num_ojects[i]].head()))



#将数值型转换为字符型变量
x['MSSubClass']=x['MSSubClass'].astype('str')


#将数值型变量缺失填充

for j in range(len(x_num_ojects)):
    x[x_num_ojects[j]]=x[x_num_ojects[j]].fillna(x[x_num_ojects[j]].mean())


#统计数值型变量是否还存在空值

x[x_num_ojects].isnull().sum().sum()



#对字符型NA填频数最大值
x_na_list={}#建立一个字典，将频数最大的放入其中
for i in x_ojects:
    if np.sum(x[i].isnull()*1)>0:
        x_na_list[i]=np.argmax(x.groupby([i])[i].count())


#建立新的自变量x_fill_na
x_fill_na=x

#对字符型缺失变量进行填充
for i in x_na_list.keys():
    x_fill_na[i]=x_fill_na[i].fillna(x_na_list[i])




#字符型变量
x_fill_na_ojects=x_fill_na.columns[x_fill_na.dtypes=='object']

#数值型变量

x_fill_na_num=x_fill_na.columns[x_fill_na.dtypes!='object']


#数值型进行标准化
#区间标准化[0，1]
x_fill_na[x_fill_na_num]=x_fill_na[x_fill_na_num].apply(lambda x:(x-np.mean(x))/(np.max(x)-np.min(x)))



#对字符型变量进行哑变量处理
x_dummies=pd.get_dummies(x_fill_na)


#拆分训练集与测试集
x_train_dummies=x_dummies.loc[house_price_train.index]

x_test_dummies=x_dummies.loc[house_price_test.index]


print("index_max:%s,index_min:%s" %(x_train_dummies.index.max(),x_train_dummies.index.min()))


print("index_max:%s,index_min:%s" %(x_test_dummies.index.max(),x_test_dummies.index.min()))



#开始建立模型
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score


alphas = np.logspace(-3,2,50)
test_scores = []
ridge_test_dict={}
for alpha in alphas:
    clf = Ridge(alpha)
    test_score = np.sqrt(-cross_val_score(clf, x_train_dummies, y, cv=10, scoring='neg_mean_squared_error'))
    test_scores.append(np.mean(test_score))
    ridge_test_dict[alpha]=np.mean(test_score)


plt.plot(alphas,test_scores)
#plt.axis([-1, 5, 0, 1])
plt.show()


ridge_result=min(ridge_test_dict.items(), key=lambda x: x[1])
print(ridge_result)
#(5.9636233165946431, 0.13507346978306825)



"""

随机森林

"""

from sklearn.ensemble import RandomForestRegressor

max_features = [.1,.2,.25,.3,.35,.4, .5, .7, .9, .99]
test_scores = []
rf_test_dict={}
for max_feat in max_features:
    clf = RandomForestRegressor(n_estimators=200, max_features=max_feat)
    test_score = np.sqrt(-cross_val_score(clf, x_train_dummies, y, cv=5, scoring='neg_mean_squared_error'))
    test_scores.append(np.mean(test_score))
    rf_test_dict[max_feat]=np.mean(test_score)


plt.plot(max_features,test_scores)
#plt.axis([-1, 5, 0, 1])
plt.show()


rf_result=min(rf_test_dict.items(), key=lambda x: x[1])
print(rf_result)
#(0.35, 0.13709999049518318)



"""

bagging算法

"""

from sklearn.ensemble import BaggingRegressor
from sklearn.model_selection import cross_val_score

ridge = Ridge(5.963)

params = [1,2,5,7,8,9, 10,12,13, 15,17,19, 20, 25, 30, 40]
test_scores = []
bagging_test_dict={}
for param in params:
    clf = BaggingRegressor(n_estimators=param, base_estimator=ridge)
    test_score = np.sqrt(-cross_val_score(clf, x_train_dummies, y, cv=20, scoring='neg_mean_squared_error'))
    test_scores.append(np.mean(test_score))
    bagging_test_dict[param]=np.mean(test_score)


plt.plot(params,test_scores)
#plt.axis([-1, 5, 0, 1])
plt.show()


bagging_result=min(bagging_test_dict.items(), key=lambda x: x[1])
print(bagging_result)
#(15, 0.13267395619942485)


"""

boosting算法,adaboost

"""

from sklearn.ensemble import AdaBoostRegressor
ridge = Ridge(3.69)
params = [1,2,5,7,8,9, 10,12,13, 15,17,19, 20, 25, 30,35, 40,45,50]
test_scores = []
adaboost_test_dict={}
for param in params:
    clf = AdaBoostRegressor(n_estimators=param, base_estimator=ridge)
    test_score = np.sqrt(-cross_val_score(clf, x_train_dummies, y, cv=20, scoring='neg_mean_squared_error'))
    test_scores.append(np.mean(test_score))
    adaboost_test_dict[param]=np.mean(test_score)



plt.plot(params,test_scores)
#plt.axis([-1, 5, 0, 1])
plt.show()


adaboost_result=min(adaboost_test_dict.items(), key=lambda x: x[1])
print(adaboost_result)
#(1, 0.1377197850989326)

"""

boosting算法,adaboost

"""
import xgboost as xgb
from xgboost import XGBRegressor
from xgboost import plot_importance
params = [1,2,3,4,5,6,7,8,9,10]
test_scores = []
xgboost_test_dict={}
for param in params:
    clf = XGBRegressor(max_depth=param)
    test_score = np.sqrt(-cross_val_score(clf, x_train_dummies, y, cv=10, scoring='neg_mean_squared_error'))
    test_scores.append(np.mean(test_score))
    xgboost_test_dict[param]=np.mean(test_score)


plt.plot(params,test_scores)
#plt.axis([-1, 5, 0, 1])
plt.show()


xgboost_result=min(xgboost_test_dict.items(), key=lambda x: x[1])
print(xgboost_result)
#(5, 0.12709021706802476)

clf = XGBRegressor(max_depth=5)
clf.fit(x_train_dummies, y)

clf.get_xgb_params

fscore=xgb.plot_importance(clf)

importance={}
for i in range(len(x_train_dummies.columns)):
    aaa=x_train_dummies.columns[i]
    importance[aaa]=clf.feature_importances_.ravel()[i]

aaa=clf.feature_importances_.ravel()[1]
bbb=x_train_dummies.columns[1]
type(aaa)
type(bbb)

result=pd.DataFrame(importance,index=[1])

result.to_csv('房价预测结果的参数.csv')

clf.evals_result_
shape(bbb)


clf.evals_result()

clf.get_booster().get_score(importance_type='weight')

predict_result=clf.predict(x_test_dummies)

predict_actual_result=np.expm1(clf.predict(x_test_dummies))

result2=pd.DataFrame({'Id':x_test_dummies.index,'SalePrice':predict_actual_result})


result2.to_excel('房价预测结果_submission.xls')

