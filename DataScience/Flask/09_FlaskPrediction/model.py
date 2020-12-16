
import pandas as pd
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
iris_dataset = load_iris()

import warnings
warnings.filterwarnings('ignore')

x_train, x_test, y_train, y_test = train_test_split(
    iris_dataset.data, iris_dataset.target, test_size=0.25, random_state=0)
#Preparing Extra Tree Regression
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=1)

knn.fit(x_train,y_train)
y_predict = knn.predict(x_test)

print("{0:.2f}, {1:.2f}".format(np.mean(y_predict == y_test), knn.score(x_test, y_test)))

import pickle
# # Saving model to disk
pickle.dump(knn, open('model.pkl', 'wb'))
model=pickle.load(open('model.pkl', 'rb'))
print(y_predict)
