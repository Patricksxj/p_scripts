# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(shenxianjun)s

#E_mail: shenxianjun.patrick@gmail.com

"""

import numpy as np
x = np.random.uniform(1, 100, 1000)
y = np.log(x) + np.random.normal(0, .3, 1000)

from matplotlib import pyplot

pyplot.plot(x,np.log(x),'r')



pyplot.scatter(x,y,c='b',s=1)

pyplot.scatter(x,np.log(x),c='r',s=3)


pyplot.show()




 """

 随机森林---回归树

 """
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
import numpy as np

from sklearn.datasets import load_iris
iris=load_iris()
#print iris#iris的４个属性是：萼片宽度　萼片长度　花瓣宽度　花瓣长度　标签是花的种类：setosa versicolour virginica
print (iris['target'].shape)
rf=RandomForestRegressor()#这里使用了默认的参数设置
rf.fit(iris.data[:150],iris.target[:150])#进行模型的训练
#
#随机挑选两个预测不相同的样本
instance=iris.data[[100,109]]
print instance
print 'instance 0 prediction；',rf.predict(instance[0])
print 'instance 1 prediction；',rf.predict(instance[1])
print iris.target[100],iris.target[109]





 """

 随机森林---分类树

 """



from sklearn.ensemble import RandomForestClassifier
iris=load_iris()
clf=RandomForestClassifier(max_depth=5, random_state=0)
clf.fit(iris.data[:150],iris.target[:150])



instance=iris.data[[110,149]]
print (instance)

print ('instance 0 prediction；',clf.predict([instance[0]]))
print ('instance 1 prediction；',clf.predict([instance[1]]))
print (iris.target[110],iris.target[149])






import numpy as np
from sklearn.metrics import roc_curve
y = iris.target[:150]
pred = clf.predict(iris.data[:150])
fpr, tpr, thresholds = roc_curve(y, pred, pos_label=2)
fpr      # array([ 0. ,  0.5,  0.5,  1. ])
tpr      # array([ 0.5,  0.5,  1. ,  1. ])
thresholds      #array([ 0.8 ,  0.4 ,  0.35,  0.1 ])
from sklearn.metrics import auc
auc(fpr, tpr)
0.75