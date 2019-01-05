# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(shenxianjun)s

#E_mail: shenxianjun.patrick@gmail.com

"""
from sklearn import svm, grid_search, datasets
iris = datasets.load_iris()
parameters = {'kernel':('linear', 'rbf'), 'C':[1, 10]}
svr = svm.SVC()
clf = grid_search.GridSearchCV(svr, parameters)
clf.fit(iris.data, iris.target)

clf.best_params_

print("Best: %f using %s" % (clf.best_score_, clf.best_params_))
for params, mean_score, scores in clf.grid_scores_:
    print("%f (%f) with: %r" % (scores.mean(), scores.std(), params))