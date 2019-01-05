# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(shenxianjun)s

#E_mail: shenxianjun.patrick@gmail.com

"""

# libraries ----
import pandas as pd
import numpy as np
import quandl
import seaborn as sns

import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import datetime as dt

import statsmodels.formula.api as smf
import statsmodels.tsa.api as smt
import statsmodels.api as sm
import scipy.stats as scs

import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='matplotlib')

# settings ----
%matplotlib inline
sns.set_style('darkgrid')
sns.mpl.rcParams['figure.figsize'] = (10.0, 6.0)
sns.mpl.rcParams['savefig.dpi'] = 90
sns.mpl.rcParams['font.size'] = 14

# authentication ----
quandl_key = 'zs7xyLhXJbVU_Sk2-4aB' # paste your own API key here :)
quandl.ApiConfig.api_key = quandl_key


# downloading the data
df = quandl.get('WIKI/MSFT', start_date="2000-01-01", end_date="2018-06-30")
df = df.loc[:, ['Adj. Close']]
df.columns = ['adj_close']

# create simple and log returns, multiplied by 100 for convenience
df['simple_rtn'] = 100 * df.adj_close.pct_change()
df['log_rtn'] = 100 * (np.log(df.adj_close) - np.log(df.adj_close.shift(1)))

# dropping NA's in the first row
df.dropna(how = 'any', inplace = True)

df.head()



# Plotting the time series ----
fig, ax =plt.subplots(3, 1, figsize=(24, 20))
# price ----
df.adj_close.plot(ax=ax[0])
ax[0].set_ylabel('Stock price ($)')
ax[0].set_xlabel('')
ax[0].set_title('Price vs. returns')
# simple returns ----
df.simple_rtn.plot(ax=ax[1])
ax[1].set_ylabel('Simple returns (%)')
ax[1].set_xlabel('')
# log returns ----
df.log_rtn.plot(ax=ax[2])
ax[2].set_ylabel('Log returns (%)')
fig.show()


# Descriptive statistics ----
print('Range of dates:', min(df.index.date), '-', max(df.index.date))
print('Number of observations:', df.shape[0])
print('Mean: {0:.4f}'.format(df.log_rtn.mean()))
print('Median: {0:.4f}'.format(df.log_rtn.median()))
print('Min: {0:.4f}'.format(df.log_rtn.min()))
print('Max: {0:.4f}'.format(df.log_rtn.max()))
print('Standard Deviation: {0:.4f}'.format(df.log_rtn.std()))
print('Skewness: {0:.4f}'.format(df.log_rtn.skew()))
print('Kurtosis: {0:.4f}'.format(df.log_rtn.kurtosis())) #Kurtosis of std. Normal dist = 0
print('Jarque-Bera statistic: {stat:.2f} with p-value: {p_val:.2f}'.format(stat = scs.jarque_bera(df.log_rtn.values)[0],
                                                                          p_val = scs.jarque_bera(df.log_rtn.values)[1]))


acf_r = smt.graphics.plot_acf(df.log_rtn, lags=40 , alpha=0.5)
acf_r.show()