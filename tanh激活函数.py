# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(shenxianjun)s

#E_mail: shenxianjun.patrick@gmail.com

"""
import math


def tanh(x):
    y=(1-exp(-2*x))/(1+exp(-2*x))
    return y

def floatrange(start,stop,steps):
    ''' Computes a range of floating value.

        Input:
            start (float)  : Start value.
            end   (float)  : End value
            steps (integer): Number of values

        Output:
            A list of floats

        Example:
            >>> print floatrange(0.25, 1.3, 5)
            [0.25, 0.51249999999999996, 0.77500000000000002, 1.0375000000000001, 1.3]
    '''
    return [start+float(i)*(stop-start)/(float(steps)-1) for i in range(steps)]


del scatter_list

scatter_list_a=[]
scatter_list_b=[]
for i in floatrange(-10.0,10.0,100000):
    scatter_list_a.append(i)
    scatter_list_b.append(tanh(i))


#tanh 激活函数图像
scatter(scatter_list_a,scatter_list_b)
plt.show()