# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(shenxianjun)s

#E_mail: shenxianjun.patrick@gmail.com

"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


crime_train_data=pd.read_csv('crime_data_train.csv',header=0,parse_dates = ['Dates'])






print(crime_train_data.head(10))





from sklearn import preprocessing
label = preprocessing.LabelEncoder()
label.fit([1, 2, 2, 6])


print(label.transform([1, 1, 2, 6]))



crime_label = label.fit_transform(crime_train_data.Category)

type(crime_label)




days = pd.get_dummies(crime_train_data.DayOfWeek)
district = pd.get_dummies(crime_train_data.PdDistrict)
hour = pd.get_dummies(crime_train_data.Dates.dt.hour)




train_data = pd.concat([days, district, hour], axis=1)
train_data['crime'] = crime_label




print(train_data.head(10))



from sklearn.cross_validation import train_test_split
training, validation = train_test_split(train_data, train_size=0.6)



from sklearn.metrics import log_loss
from sklearn.naive_bayes import BernoulliNB
model = BernoulliNB()
feature_list = training.columns.tolist()
feature_list = feature_list[:len(feature_list) - 1]
print('选取的特征列：', feature_list)
model.fit(training[feature_list], training['crime'])
predicted = np.array(model.predict_proba(validation[feature_list]))
print("朴素贝叶斯log损失为 %f" % (log_loss(validation['crime'], predicted)))



from sklearn.linear_model import LogisticRegression
model = LogisticRegression(C=0.1)
model.fit(training[feature_list], training['crime'])
predicted = np.array(model.predict_proba(validation[feature_list]))
print("逻辑回归log损失为 %f" %(log_loss(validation['crime'], predicted)))





crime_label.groupby(['0'])['0'].count()



crime_train_data.columns

crime_train_data['Category'].isnull().sum()

crime_train_data.Category.count()

crime_train_data.groupby(['Category'])['Category'].count()