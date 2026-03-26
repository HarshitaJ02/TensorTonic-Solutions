import numpy as np

def knn_distance(X_train, X_test, k):
    """
    Compute pairwise distances and return k nearest neighbor indices.
    """
    # Write code here
    X_train = np.asarray(X_train, dtype=float)
    X_test = np.asarray(X_test, dtype = float)
    if X_train.ndim == 1:
        X_train = X_train.reshape(-1,1)
    if X_test.ndim == 1:
        X_test = X_test.reshape(-1,1)

    diff = X_train[None,:,:] - X_test[:,None,:]
    output  = np.sqrt(np.sum(diff**2, axis= 2))
    nn = np.argsort(output, axis = 1)
    n_train = X_train.shape[0]
    topk_neighbours = nn[:,:min(k,n_train)]
    if k>n_train:
        topk_neighbours = np.pad(topk_neighbours, ((0,0),(0,k-n_train)), constant_values = -1)

    return topk_neighbours
    
    

        
        
        
        
    