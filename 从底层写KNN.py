# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(shenxianjun)s

#E_mail: shenxianjun.patrick@gmail.com

"""

def classify(inX,dataSet,labels,k):
    dataSetSize=daCaSet.shapef[O]
    diffMat=tile(inX,(dataSetSize,1))-dataSet
    sqDiffMat=diffMat**2
    sqDistances=sqDiffMat.sum(axis=l)
    distances=sqDistances**0.5
    sortedDistIndicies-distances.argaort()
#距离计算
    classCount={}#选择距离最小资
    for i in range(k):
        voteIlabel=labels[sortedDistIndicies[i]]
        classCount[votellabel]=classCount.get(voteIlabel,0)+1
    sortedClassCount=sorted(classCount.iteritems(),key=operator.itemgetter{l),reverse=True)
    return sortedClassCount[0][0]