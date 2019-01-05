import xgboost
import numpy
from numpy import loadtxt
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.neighbors import KNeighborsClassifier
from xgboost import plot_importance
from matplotlib import pyplot
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import StratifiedKFold
dataset=loadtxt(r'G:\统计类知识与材料\唐宇迪\01【非加密】python数据分析与机器学习实战\课程资料\唐宇迪-机器学习课程资料\补充的内容\Xgboost\pima-indians-diabetes.csv',delimiter=",")

X=dataset[:,0:8]
Y=dataset[:,8]
#print(Y)

X_train,X_test,y_train,y_test=train_test_split(X,Y,test_size=0.3,random_state=12345)

'''
xgboost参数优化:
learning_rate
tree
n_estimator
max_depth
min_child_weight
subsample,colsample_bytree
gamma

正则化参数
lambda
alpha



'''

model=XGBClassifier(learning_rate=0.1,n_estimators=1000,max_depth=5,min_child_weight=1,gamma=0.01,subsample=0.8,colsample_bytree=0.8,objective='binary:logistic',nthread=4,scale_pos_weight=1,seed=27)
model.fit(X_train,y_train,early_stopping_rounds=15,eval_metric='logloss',eval_set=[(X_test,y_test)],verbose=True)
y_pred=model.predict(X_test)

prediction=[round(value) for value in y_pred]
accuracy=accuracy_score(prediction,y_test)
print('xgboost_accuracy:%.2f%%' %(accuracy*100.00))
plot_importance(model)
pyplot.show()




'''
gbdt
'''
clf=GradientBoostingClassifier()
clf.fit(X_train,y_train)
y_pred2=clf.predict(X_test)

prediction2=[round(value) for value in y_pred2]
accuracy2=accuracy_score(prediction2,y_test)
print('gbdt_accuracy:%.2f%%' %(accuracy2*100.00))

'''
KNN
'''

clf2=KNeighborsClassifier()
clf2.fit(X_train,y_train)
y_pred3=clf2.predict(X_test)

prediction3=[round(value) for value in y_pred3]
accuracy3=accuracy_score(prediction3,y_test)
print('KNN_accuracy:%.2f%%' %(accuracy3*100.00))

'''
AdaBoost
'''
clf3=AdaBoostClassifier()
clf3.fit(X_train,y_train)
y_pred4=clf3.predict(X_test)

prediction4=[round(value) for value in y_pred4]
accuracy4=accuracy_score(prediction4,y_test)
print('AdaBoost_accuracy:%.2f%%' %(accuracy4*100.00))