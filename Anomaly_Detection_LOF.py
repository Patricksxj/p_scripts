import time
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

from sklearn.neighbors import LocalOutlierFactor




import os
#print(os.getcwd())
df = pd.read_csv(r'D:\P_WORKPLACE\TimeSeriesExpedia.csv')
outliers_fraction=0.01





data = df[['price_usd', 'srch_booking_window', 'srch_saturday_night_bool']]
scaler = StandardScaler()
np_scaled = scaler.fit_transform(data)
data = pd.DataFrame(np_scaled)
# train isolation forest
model =  LocalOutlierFactor(n_neighbors=35, contamination=outliers_fraction)
model.fit(data)

df['anomaly5'] = pd.Series(model.fit_predict(data))
# df['anomaly2'] = df['anomaly2'].map( {1: 0, -1: 1} )

fig, ax = plt.subplots(figsize=(10,6))

df['date_time'] = pd.to_datetime(df['date_time'])
df = df.sort_values('date_time')
df['date_time_int'] = df.date_time.astype(np.int64)
a = df.loc[df['anomaly5'] == -1, ['date_time_int', 'price_usd']] #anomaly

ax.plot(df['date_time_int'], df['price_usd'], color='blue', label = 'Normal')
ax.scatter(a['date_time_int'],a['price_usd'], color='red', label = 'Anomaly')
plt.legend()
plt.show()


print(df.groupby(['anomaly5'])['anomaly5'].count())



