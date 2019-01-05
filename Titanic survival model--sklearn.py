# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(shenxianjun)s

#E_mail: shenxianjun.patrick@gmail.com

"""
#
#from sklearn.preprocessing import OneHotEncoder
#enc = OneHotEncoder()
#enc.fit([[0, 0, 3], [1, 1, 0], [0, 2, 1], [1, 0, 2]])
#
#
#enc.n_values_
#
#enc.feature_indices_
#
#enc.transform([[0, 1, 1]]).toarray()

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

train_data=pd.read_csv(r'train.csv',header=0)

test_data=pd.read_csv(r'test.csv',header=0)


#x=raw_data.loc[:,['PassengerId','Pclass','Name','Sex','Age','SibSp','Parch','Ticket	Fare','Cabin','Embarked']]
#
#y=raw_data.loc[:,'Survived']


#x_train,x_test,y_train,y_test=train_test_split(x, y,train_size=0.7)


shape(train_data)

train_data.describe().T


#1)train data
#对年龄为空的数据进行填充

train_data[train_data['Age'].isnull()]['Age'].head()

train_data['Age']=train_data['Age'].fillna(train_data['Age'].mean())


train_data[train_data['Age'].isnull()]['Age'].head()


#对测试集数据进行填充
test_data[test_data['Age'].isnull()]['Age']

test_data['Age']=test_data['Age'].fillna(test_data['Age'].mean())



# family特征
train_data['Family_Size'] = train_data['SibSp'] + train_data['Parch']
train_data['Family'] = train_data['SibSp'] * train_data['Parch']

test_data['Family_Size'] = test_data['SibSp'] + test_data['Parch']
test_data['Family'] = test_data['SibSp'] * test_data['Parch']




#对登船港口为空的进行填充

train_data.Embarked = train_data['Embarked'].fillna('S')
test_data.Embarked = test_data['Embarked'].fillna('S')

train_data[train_data['Embarked'].isnull()]


#对费用为空值的填充
train_data.Fare=train_data.Fare.fillna(train_data.Fare.mean())


test_data.Fare=test_data.Fare.fillna(test_data.Fare.mean())


# 处理训练集

#字符型变量做哑变量
Pclass = pd.get_dummies(train_data.Pclass)
Sex = pd.get_dummies(train_data.Sex)
Embarked = pd.get_dummies(train_data.Embarked)
#Title = pd.get_dummies(train_data.Title)
#AgeCat = pd.get_dummies(train_data.AgeCat)
#HighLow = pd.get_dummies(train_data.HighLow)
train_data_new = pd.concat([Pclass, Sex, Embarked], axis=1)


#数值型变量
train_data_new['Age'] = train_data['Age']
train_data_new['Fare'] = train_data['Fare']
train_data_new['SibSp'] = train_data['SibSp']
train_data_new['Parch'] = train_data['Parch']
train_data_new['Family_Size'] = train_data['Family_Size']
train_data_new['Family'] = train_data['Family']
#train_data_new['AgeFill'] = train_data['AgeFill']
#train_data_new['Fare_Per_Person'] = train_data['Fare_Per_Person']
#train_data_new['Cabin'] = train_data['Cabin']
#train_data_new['AgeClass'] = train_data['AgeClass']
#train_data_new['ClassFare'] = train_data['ClassFare']


cols = ['Age', 'Fare', 'SibSp', 'Parch', 'Family_Size', 'Family']
train_data_new[cols] = train_data_new[cols].apply(lambda x: (x - np.mean(x)) / (np.max(x) - np.min(x)))
print(train_data_new.head())

shape(train_data_new)




#处理测试集合

Pclass = pd.get_dummies(test_data.Pclass)
Sex = pd.get_dummies(test_data.Sex)
Embarked = pd.get_dummies(test_data.Embarked)
#Title = pd.get_dummies(test_data.Title)
#AgeCat = pd.get_dummies(test_data.AgeCat)
#HighLow = pd.get_dummies(test_data.HighLow)
test_data_new = pd.concat([Pclass, Sex, Embarked], axis=1)


#数值型变量
test_data_new['Age'] = test_data['Age']
test_data_new['Fare'] = test_data['Fare']
test_data_new['SibSp'] = test_data['SibSp']
test_data_new['Parch'] = test_data['Parch']
test_data_new['Family_Size'] = test_data['Family_Size']
test_data_new['Family'] = test_data['Family']
#test_data_new['AgeFill'] = test_data['AgeFill']
#test_data_new['Fare_Per_Person'] = test_data['Fare_Per_Person']
#test_data_new['Cabin'] = test_data['Cabin']
#test_data_new['AgeClass'] = test_data['AgeClass']
#test_data_new['ClassFare'] = test_data['ClassFare']



cols = ['Age', 'Fare', 'SibSp', 'Parch', 'Family_Size', 'Family']
test_data_new[cols] = test_data_new[cols].apply(lambda x: (x - np.mean(x)) / (np.max(x) - np.min(x)))
print(test_data_new.head())
shape(test_data_new)




#开始训练模型


from sklearn.linear_model import LogisticRegression as LR
from sklearn.cross_validation import cross_val_score
from sklearn.naive_bayes import GaussianNB as GNB
from sklearn.ensemble import RandomForestClassifier
import numpy as np

label = train_data['Survived']
model_lr = LR(penalty = 'l2', dual = True, random_state = 0,max_iter=1000)
model_lr.fit(train_data_new, label)

print("逻辑回归15折交叉验证得分: ", np.mean(cross_val_score(model_lr, train_data_new, label, cv=15, scoring='roc_auc')))

model_lr.coef_

model_lr.intercept_

model_lr.get_params()

result = model_lr.predict(test_data_new)


#test_data_new.to_csv('test_data_new.csv')


output = pd.DataFrame( data={"PassengerId":test_data["PassengerId"], "Survived":result} )
output.to_csv( "lr.csv", index=False, quoting=3 )