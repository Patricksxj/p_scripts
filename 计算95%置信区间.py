# 使用该方法，计算的是95%CI
# 计算95%CI时，网上有人设置 alpha=0.05， 不正确
# 注意：scale不是标注差，是标准误差
# 在查 Z 表的時候，首先要先看檢定是單尾檢定還是雙尾檢定 。如果是求信賴區間的話就是雙尾檢定 。
import numpy as np
from scipy.stats import *
data=np.random.normal(0,1,10000)
confidence=0.95
result=t.interval(confidence,df=len(data) - 1,loc=data.mean(),scale=sem(data))
mean=data.mean()
std=data.std()
a=mean-1.96*std/np.sqrt(len(data))
b=mean+1.96*std/np.sqrt(len(data))
print("用公式计算出的置信区间：",result)
print("手工计算结果,下限",a)
print("手工计算结果,上限",b)
