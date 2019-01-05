# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(shenxianjun)s

#E_mail: shenxianjun.patrick@gmail.com

"""
import math

a=2
math.sqrt(a)

for a in range(0,10000):
    for b in range(0,10000):
        if math.sqrt(a)+math.sqrt(b)==math.sqrt(1998):
            print('a={},b={},a+b={}'.format(a,b,a+b))
        else:
            pass

