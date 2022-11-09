# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 12:35:25 2020

@author: Kasia
"""

import numpy as np, random, scipy.stats as ss
import pandas as pd

def majority_vote_fast(votes):
    mode, count = ss.mstats.mode(votes)
    return mode

def distance(p1, p2):
    return np.sqrt(np.sum(np.power(p2 - p1, 2)))

def find_nearest_neighbors(p, points, k=5):
    distances = np.zeros(points.shape[0])
    for i in range(len(distances)):
        distances[i] = distance(p, points[i])
    ind = np.argsort(distances)
    return ind[:k]

def knn_predict(p, points, outcomes, k=5):
    ind = find_nearest_neighbors(p, points, k)
    return majority_vote_fast(outcomes[ind])[0]

data = pd.read_csv("wines.csv", index_col=0)

#def check_color(row):
#    if row['color'] == 'red':
#        is_red = 1
#    elif (row['color']) == 'white':
#        is_red = 0
#    return is_red
#data['is_red'] = data.apply(check_color, axis=1)
#numeric_data = data.drop(columns=['color'])

data["is_red"] = (data["color"] == "red").astype(int)
numeric_data = data.drop("color", axis=1)
#print(data.groupby('is_red').count())

#Scale the data using the sklearn.preprocessing function scale() on numeric_data.
#Convert this to a pandas dataframe, and store as numeric_data.
#Include the numeric variable names using the parameter columns = numeric_data.columns.
#Use the sklearn.decomposition module PCA() and store it as pca.
#Use the fit_transform() function to extract the first two principal components 
#from the data, and store them as principal_components.
#Note: You may get a DataConversionWarning, but you can safely ignore it
import sklearn.preprocessing
scaled_data = sklearn.preprocessing.scale(numeric_data)
numeric_data = pd.DataFrame(scaled_data, columns = numeric_data.columns)

import sklearn.decomposition
pca = sklearn.decomposition.PCA(n_components = 2)
principal_components = pca.fit_transform(numeric_data)

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.backends.backend_pdf import PdfPages
observation_colormap = ListedColormap(['red', 'blue'])
x = principal_components[:,0]
y = principal_components[:,1]

plt.title("Principal Components of Wine")
plt.scatter(x, y, alpha = 0.2,
    c = data['high_quality'], cmap = observation_colormap, edgecolors = 'none')
plt.xlim(-8, 8); plt.ylim(-8, 8)
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.show()

def accuracy(predictions, outcomes):
    """Takes two lists of the same size as arguments and returns a single number, 
    which is the percentage of elements that are equal for the two lists."""
    match = 100*np.mean(predictions == outcomes)
    return match

#print(accuracy(0,data["high_quality"]))  #simple classifier - wines in the dataset of low quality(0)

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 5)
knn.fit(numeric_data, data['high_quality'])
library_predictions = knn.predict(numeric_data)
#accuracy(library_predictions, data["high_quality"]) #classifier using knn-prediction

n_rows = data.shape[0]
random.seed(123)
selection = random.sample(range(n_rows), 10)
predictors = np.array(numeric_data)

training_indices = [i for i in range(len(predictors)) if i not in selection]
outcomes = np.array(data["high_quality"])

my_predictions = np.array([knn_predict(p, predictors, outcomes, k=5) for p in predictors[selection]])
data_outcome = (data.high_quality[selection]).tolist()[:10]
percentage = accuracy(my_predictions, data_outcome)
print(percentage)