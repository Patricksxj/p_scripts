# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(shenxianjun)s

#E_mail: shenxianjun.patrick@gmail.com

"""

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn import datasets,tree
import pandas as pd
import numpy as np
import pydotplus
from sklearn.externals.six import StringIO
from sklearn.tree import export_graphviz

"""
def rf_model(num=5):
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['is_train'] = np.random.uniform(0, 1, len(df)) <= .75
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

    train, test = df[df['is_train']==True], df[df['is_train']==False]

    features = df.columns[:4]
    clf = RandomForestClassifier(n_jobs=num)
    y,_= pd.factorize(train['species'])
    clf.fit(train[features], y)
    preds = iris.target_names[clf.predict(test[features])]
    y1,_=pd.factorize(np.array(test['species']))
    pred1 = clf.predict(test[features])
    from sklearn.metrics import roc_curve,auc
    fpr, tpr, thresholds = roc_curve(y1, pred1, pos_label=2)
    print('THE %d trees roc result is:%1.2f)' %(num,auc(fpr, tpr)))
"""
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['is_train'] = np.random.uniform(0, 1, len(df)) <= .75
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

train, test = df[df['is_train']==True], df[df['is_train']==False]

features = df.columns[:4]
clf = RandomForestClassifier(n_jobs=20)
y,_= pd.factorize(train['species'])
clf.fit(train[features], y)
preds = iris.target_names[clf.predict(test[features])]
y1,_=pd.factorize(np.array(test['species']))
pred1 = clf.predict(test[features])
from sklearn.metrics import roc_curve,auc
fpr, tpr, thresholds = roc_curve(y1, pred1, pos_label=2)
print('THE %d trees roc result is:%1.2f)' %(20,auc(fpr, tpr)))

"""
for i in range(10,200):
    rf_model(num=i)
"""
tree_in_forest = clf.estimators_[0]
dot_data = StringIO()
tree.export_graphviz(tree_in_forest, out_file=dot_data)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf("irisacc.pdf")
