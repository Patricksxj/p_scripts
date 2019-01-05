# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(shenxianjun)s

#E_mail: shenxianjun.patrick@gmail.com

"""
import numpy as np
from scipy.stats import binom
import scipy
import matplotlib.pyplot as plt

import scipy
n=100
p=0.25
k=np.arange(60,100)
binormal=binom.pmf(k,n,p)#100题中正好对了60题的概率
print(binormal)





# ⑤伪造符合二项分布的随机变量 (random variates)
X = scipy.stats.binom.rvs(n,p,size=20)
#array([2, 3, 1, 2, 2, 2, 1, 2, 2, 3, 3, 0, 1, 1, 1, 2, 3, 4, 0, 3])

#⑧作出上面满足二项分布随机变量的频数直方图（类似group by）
plt.hist(X)
