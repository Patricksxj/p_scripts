# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(shenxianjun)s

#E_mail: shenxianjun.patrick@gmail.com

"""

import pandas as pd
wine = pd.read_csv('wine_data.csv', names = ["Cultivator", "Alchol", "Malic_Acid", "Ash", "Alcalinity_of_Ash", "Magnesium", "Total_phenols", "Falvanoids", "Nonflavanoid_phenols", "Proanthocyanins", "Color_intensity", "Hue", "OD280", "Proline"])



wine.head()

wine.describe().transpose()

x=wine.drop('Cultivator',axis=1)
y=wine['Cultivator']


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(x, y,train_size=0.7)

X_train.shape, X_test.shape

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

scaler.fit(X_train)

# Now apply the transformations to the data:
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.neural_network import MLPClassifier

mlp = MLPClassifier(hidden_layer_sizes=(13,13,13),max_iter=1500)

mlp.fit(X_train,y_train)


predictions = mlp.predict(X_test)

from sklearn.metrics import classification_report,confusion_matrix


print(confusion_matrix(y_test,predictions))

print(classification_report(y_test,predictions))

coefs=mlp.coefs_

len(coefs)

intercepts_=mlp.intercepts_

t10=X_test[15]

y_test[14:15]


predictions_10 = mlp.predict([t10])