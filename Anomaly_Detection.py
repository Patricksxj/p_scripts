import pandas as pd
import numpy as np
import matplotlib.dates as md
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.covariance import EllipticEnvelope
from pyemma import msm
from sklearn.ensemble import IsolationForest
from sklearn.svm import OneClassSVM
from mpl_toolkits.mplot3d import Axes3D
from pyemma import msm


import os
#print(os.getcwd())
os.chdir(r'G:\统计类知识与材料\数据集\expedia-personalized-sort')
#print(os.getcwd())
expedia = pd.read_csv('./train.csv')

#数据集为美国的某一个酒店
df=expedia[expedia['prop_id']==104517]
df = df.loc[df['srch_room_count'] == 1]
df = df.loc[df['visitor_location_country_id'] == 219]
df = df[['date_time', 'price_usd', 'srch_booking_window', 'srch_saturday_night_bool']]

#删除导入数据集
del expedia

#转换为时间格式
df['date_time'] = pd.to_datetime(df['date_time'])
df = df.sort_values('date_time')

#发现有极端值
df['price_usd'].describe()

#去除极端值
df = df.loc[df['price_usd'] < 5584]

#导出数据集
df.to_csv(r'D:\P_WORKPLACE\TimeSeriesExpedia.csv', index=False)

