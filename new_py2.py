from sklearn.model_selection import train_test_split
from pandas import DataFrame
from sklearn import metrics
from sklearn.datasets  import  make_hastie_10_2
from xgboost.sklearn import XGBClassifier
import xgboost as xgb

import seaborn

import seaborn as sns
from matplotlib import pyplot as plt
#导入数据
titanic = sns.load_dataset('titanic')
#做一些简单的缺失值处理
titanic = titanic.drop('deck', axis=1)
titanic['age'].fillna(titanic['age'].median(), inplace=True)
titanic['embark_town'].fillna(titanic['embark_town'].mode()[0], inplace=True)
titanic['embarked'].fillna(titanic['embarked'].mode()[0], inplace=True)