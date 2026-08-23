# implement k means

# unsupervised way to cluster 
# k groups
# minimise the distance from all points to their closest centre
# sum of L2 distance, square sum of distances 

### algorithm
# randomly start with k points
# calculate L2 distance from all pints to current centre
# update new centres - take the mean of each current cluster 
# check centres change minimal


import numpy as np

def k_means(k, X, max_iter=10):
    # X - (n, d)
    n = X.shape[0]

    # randomly start with k points
    centers = X[np.random.choice(n, k, replace = False)]  # (k, d)

    # for each iterative steps, calculate L2 distance from all points to current centre
    for _ in range(max_iter):
        # (n, 1, d) - (1, k, d) -> (n, k, d)
        distances = ((X[:, np.newaxis, :] - centers[np.newaxis, :, :]) ** 2).sum(axis=2) # (n, k)
        labels = np.argmin(distances, axis = 1) # (n, 1)

        # update new centres - take the mean of each current cluster 
        new_centers = np.array(X[labels == i] for i in range(k))

        # check centres change minimal
        if np.all(centers == new_centers):
            break

        centers = new_centers

    return centers


