# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(shenxianjun)s

#E_mail: shenxianjun.patrick@gmail.com

"""

from xgboost import XGBClassifier

import numpy as np
training_data = np.load(r"C:\Users\Administrator\Desktop\text-classification\training_data.npy")
training_data.shape


training_labels = np.load(r"C:\Users\Administrator\Desktop\text-classification\training_labels.npy")
training_labels

training_labels.shape


test_data = np.load(r"C:\Users\Administrator\Desktop\text-classification\test_data.npy")
test_data.shape


test_labels = np.load(r"C:\Users\Administrator\Desktop\text-classification\test_labels.npy")
test_labels.shape



from sklearn.ensemble import GradientBoostingClassifier
gbdt = GradientBoostingClassifier()
gbdt.fit(training_data, training_labels)  # 训练。喝杯咖啡吧

gbdt.feature_importances_   # 据此选取重要的特征

gbdt.feature_importances_.shape
