import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
import pandas as pd
import pickle



# Importing the dataset
dataset = pd.read_csv('test.csv')
X = dataset.iloc[:, [0, 1, 2]].values
Y = dataset.iloc[:, 3].values

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=0)

# Feature Scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Fitting Random Forest Classification to the Training set

classifier = RandomForestClassifier(n_estimators=10, criterion='entropy', random_state=0)
classifier.fit(X_train, Y_train)
pickle.dump(classifier, open("./pickles/random_forest.pickle", 'wb'))




# Fitting Naive Bayes to the Training set

classifier = GaussianNB()
classifier.fit(X_train, Y_train)
pickle.dump(classifier, open("./pickles/naive_bayes.pickle", 'wb'))


# Fitting K-NN to the Training set

classifier = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2)
classifier.fit(X_train, Y_train)
pickle.dump(classifier, open("./pickles/knn.pickle", 'wb'))


# Fitting Decision Tree Classification to the Training set

classifier = DecisionTreeClassifier(criterion='entropy', random_state=0)
classifier.fit(X_train, Y_train)
pickle.dump(classifier, open("./pickles/decision_tree.pickle", 'wb'))

