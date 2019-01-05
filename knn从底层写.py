# coding:utf-8


#-*-coding:utf-8 -*-
import sys
sys.path.append("D:\p_scripts")
import KNN
from numpy import *
dataSet,labels = KNN.createDataSet()
input = array([1.1,.3])
K = 3
output = KNN.classify(input,dataSet,labels,K)
print("测试数据为:",input,"分类结果为：",output)