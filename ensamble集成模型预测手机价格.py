# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(shenxianjun)s

#E_mail: shenxianjun.patrick@gmail.com

"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

from sklearn.preprocessing import OneHotEncoder,StandardScaler

df=pd.read_csv('phone_price_predict.csv',header=0)

aaa=df.columns
char_column_list=['blue','four_g','three_g','touch_screen','wifi']

num_column_list=['battery_power','clock_speed',	'dual_sim',	'fc',	'int_memory',	'm_dep',	'mobile_wt',	'n_cores',	'pc',	'px_height',	'px_width',	'ram',	'sc_h',	'sc_w',	'talk_time']



#对样本进行拆分
X_train,x_test,y_train,y_test=train_test_split(df.drop('price_range',axis=1),df['price_range'],test_size=0.2,random_state=100)




enc = OneHotEncoder(sparse=False)
enc_train_cat_feats=enc.fit_transform(X_train[char_column_list].values)

enc_test_cat_feats=enc.transform(x_test[char_column_list].values)



train_numeric_feats=X_train[num_column_list]


test_numeric_feats=x_test[num_column_list]


train_all_feats = np.hstack((train_numeric_feats, enc_train_cat_feats))
test_all_feats = np.hstack((test_numeric_feats, enc_test_cat_feats))

   # 标准化
std_scaler = StandardScaler()
scaled_trn_all_feats = std_scaler.fit_transform(train_all_feats)
scaled_tes_all_feats = std_scaler.transform(test_all_feats)




from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import AdaBoostClassifier, GradientBoostingClassifier, RandomForestClassifier
from mlxtend.classifier import StackingClassifier
from sklearn.model_selection import GridSearchCV
import time


sclf = StackingClassifier(classifiers=[KNeighborsClassifier(),
                                           SVC(kernel='rbf'),
                                           DecisionTreeClassifier()],
                              meta_classifier=LogisticRegression())

model_name_param_dict = {'kNN': (KNeighborsClassifier(),
                                     {'n_neighbors': [1,2,5,10,15,20,30,40,50]}),
                             'LR': (LogisticRegression(),
                                    {'C': [0.01, 1,10,50, 100]}),
                             'SVM': (SVC(kernel='rbf'),
                                     {'C': [0.01, 1,10,50, 100]}),
                             'DT': (DecisionTreeClassifier(),
                                    {'max_depth': [10,30,50, 100,120, 150]}),
                             'Stacking': (sclf,
                                          {'kneighborsclassifier__n_neighbors': [5, 25, 55],
                                           'svc__C': [0.01, 1, 100],
                                           'decisiontreeclassifier__max_depth': [50, 100, 150],
                                           'meta-logisticregression__C': [0.01, 1, 100]}),
                             'AdaBoost': (AdaBoostClassifier(),
                                          {'n_estimators': [10,30,50, 100,120, 150,200]}),
                             'GBDT': (GradientBoostingClassifier(),
                                      {'learning_rate': [0.01, 0.1, 1, 10,50, 100]}),
                             'RF': (RandomForestClassifier(),
                                    {'n_estimators': [1,10,50,100, 150, 200, 250]})}

    # 比较结果的DataFrame
results_df = pd.DataFrame(columns=['Accuracy (%)', 'Time (s)'],
                              index=list(model_name_param_dict.keys()))
results_df.index.name = 'Model'

for model_name, (model, param_range) in model_name_param_dict.items():
    clf = GridSearchCV(estimator=model,
                       param_grid=param_range,
                       cv=5,
                       scoring='accuracy',
                       refit=True)
    start = time.time()
    clf.fit(scaled_trn_all_feats, y_train)
    # 计时
    end = time.time()
    mean_duration = end - start
    best_acc = clf.score(scaled_tes_all_feats, y_test)

    results_df.loc[model_name, 'Accuracy (%)'] = best_acc * 100
    results_df.loc[model_name, 'Time (s)'] = mean_duration


#可视化！
from sklearn import tree
import pydotplus
del clf

parameters={'learning_rate': [0.01, 0.1, 1, 10,50, 100]}
grid = GridSearchCV(GradientBoostingClassifier(),
                       parameters,
                       cv=5,
                       scoring='accuracy',
                       refit=True)

grid=grid.fit(scaled_trn_all_feats, y_train)

clf=GradientBoostingClassifier(criterion='friedman_mse', init=None,
              learning_rate=0.1, loss='deviance', max_depth=3,
              max_features=None, max_leaf_nodes=None,
              min_impurity_decrease=0.0, min_impurity_split=None,
              min_samples_leaf=1, min_samples_split=2,
              min_weight_fraction_leaf=0.0, n_estimators=100,
              presort='auto', random_state=None, subsample=1.0, verbose=0,
              warm_start=False)

clf=clf.fit(scaled_trn_all_feats, y_train)
clf.



import pydotplus
from sklearn import tree

for i in range(clf.estimators_.shape[0]):
    dot_data = tree.export_graphviz(clf.estimators_[i][0], out_file=None)
    graph = pydotplus.graph_from_dot_data(dot_data)
    graph.write_pdf("tree_"+str(i)+".pdf")
