import numpy as np
import math

class KNearestNeighbor:

    def __init__(self):
        pass

    def fit(self, X, y):

        self.X_train = X # numpy array shape (num_train, 64)
        self.y_train = y # numpy array shape (num_train,)
      
    def compute_distances_two_loops(self, X):

        num_train = self.X_train.shape[0]
        num_test = X.shape[0] 
        dists = mp.zeros((num_test, num_train))
        for i in range(num_test):
            for j in range(num_train):
                dists[i][j] = math.sqrt((X_test[i])**2 + (X_train[j])**2)

        return dists     



