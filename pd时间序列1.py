import pandas as pd
import numpy as np
range=pd.date_range('2018/12/01',periods=90,freq='D')
print(range)
ts=pd.Series(np.random.rand(len(range)),index=range)
re_ts=ts.resample('3d').sum()
print('3day_freq',re_ts)
re_ts2=re_ts.resample('D').bfill()
print(re_ts2)

print(re_ts.resample('D').asfreq())