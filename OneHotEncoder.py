# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(shenxianjun)s

#E_mail: shenxianjun.patrick@gmail.com

"""

from sklearn.preprocessing import OneHotEncoder
enc = OneHotEncoder()
enc.fit([[0, 0, 3], [1, 1, 0], [0, 2, 1], [1, 0, 2]])


enc.n_values_

enc.feature_indices_

enc.transform([[0, 1, 1]]).toarray()

print("the onhotcodeer is : %s" %(' 1 0 | 0 1 0 |0 1 0 0'))

"""
result is :

 1 0 | 0 1 0 |0 1 0 0

 """