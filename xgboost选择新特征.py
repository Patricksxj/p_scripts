# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(shenxianjun)s

#E_mail: shenxianjun.patrick@gmail.com

"""

from sklearn.model_selection import train_test_split
from pandas import DataFrame
from sklearn import metrics
from sklearn.datasets  import  make_hastie_10_2
from xgboost.sklearn import XGBClassifier
import xgboost as xgb


#准备数据，y本来是[-1:1],xgboost自带接口邀请标签是[0:1],把-1的转成1了。
X, y = make_hastie_10_2(random_state=0)
X = DataFrame(X)
y = DataFrame(y)
y.columns={"label"}
label={-1:0,1:1}
y.label=y.label.map(label)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)#划分数据集
y_train.head()

#XGBoost自带接口
params={
    'eta': 0.3,
    'max_depth':3,
    'min_child_weight':1,
    'gamma':0.3,
    'subsample':0.8,
    'colsample_bytree':0.8,
    'booster':'gbtree',
    'objective': 'binary:logistic',
    'nthread':12,
    'scale_pos_weight': 1,
    'lambda':1,
    'seed':27,
    'silent':0 ,
    'eval_metric': 'auc'
}
d_train = xgb.DMatrix(X_train, label=y_train)
d_valid = xgb.DMatrix(X_test, label=y_test)
d_test = xgb.DMatrix(X_test)
watchlist = [(d_train, 'train'), (d_valid, 'valid')]

#sklearn接口
clf = XGBClassifier(
    n_estimators=30,#三十棵树
    learning_rate =0.3,
    max_depth=3,
    min_child_weight=1,
    gamma=0.3,
    subsample=0.8,
    colsample_bytree=0.8,
    objective= 'binary:logistic',
    nthread=12,
    scale_pos_weight=1,
    reg_lambda=1,
    seed=27)

model_bst = xgb.train(params, d_train, 30, watchlist, early_stopping_rounds=500, verbose_eval=10)
model_sklearn=clf.fit(X_train, y_train)

y_bst= model_bst.predict(d_test)
y_sklearn= clf.predict_proba(X_test)[:,1]


print("XGBoost_自带接口    AUC Score : %f" % metrics.roc_auc_score(y_test, y_bst))
print("XGBoost_sklearn接口 AUC Score : %f" % metrics.roc_auc_score(y_test, y_sklearn))

print("原始train大小：",X_train.shape)
print("原始test大小：",X_test.shape)

##XGBoost自带接口生成的新特征
train_new_feature= model_bst.predict(d_train, pred_leaf=True)
test_new_feature= model_bst.predict(d_test, pred_leaf=True)
train_new_feature1 = DataFrame(train_new_feature)
test_new_feature1 = DataFrame(test_new_feature)
print("新的特征集(自带接口)：",train_new_feature1.shape)
print("新的测试集(自带接口)：",test_new_feature1.shape)

#sklearn接口生成的新特征
train_new_feature= clf.apply(X_train)#每个样本在每颗树叶子节点的索引值
test_new_feature= clf.apply(X_test)
train_new_feature2 = DataFrame(train_new_feature)
test_new_feature2 = DataFrame(test_new_feature)

print("新的特征集(sklearn接口)：",train_new_feature2.shape)
print("新的测试集(sklearn接口)：",test_new_feature2.shape)

train_new_feature1.head()


#用两组新的特征分别训练，预测

#用XGBoost自带接口生成的新特征训练
new_feature1=clf.fit(train_new_feature1, y_train)
y_new_feature1= clf.predict_proba(test_new_feature1)[:,1]
#用XGBoost自带接口生成的新特征训练
new_feature2=clf.fit(train_new_feature2, y_train)
y_new_feature2= clf.predict_proba(test_new_feature2)[:,1]


print("XGBoost自带接口生成的新特征预测结果 AUC Score : %f" % metrics.roc_auc_score(y_test, y_new_feature1))
print("XGBoost自带接口生成的新特征预测结果 AUC Score : %f" % metrics.roc_auc_score(y_test, y_new_feature2))



from xgboost import plot_tree
from xgboost import plot_importance
import matplotlib.pyplot as plt
from graphviz import Digraph
import pydot

#model_bst = xgb.train(params, d_train, 30, watchlist, early_stopping_rounds=500, verbose_eval=10)
#model_sklearn=clf.fit(X_train, y_train)

#model_bst
plot_tree(model_bst, num_trees=0)
plot_importance(model_bst)
plt.show()

#model_sklearn:
plot_tree(model_sklearn)
plot_importance(model_sklearn)
plt.show()



def ceate_feature_map(features):
    outfile = open('xgb.fmap', 'w')
    i = 0
    for feat in features:
        outfile.write('{0}\t{1}\tq\n'.format(i, feat))
        i = i + 1
    outfile.close()
ceate_feature_map(X_train.columns)#特征名列表


xgb.plot_tree(model_bst,fmap='xgb.fmap')

fig,ax = plt.subplots()
fig.set_size_inches(60,30)
xgb.plot_tree(model_bst,ax = ax,fmap='xgb.fmap')

fig

fig.savefig('xgb_tree.jpg')