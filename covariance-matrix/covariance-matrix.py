import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here
    X= np.asarray(X, dtype = float)
    if X.ndim != 2 or X.shape[0] < 2:
        return None
    mu = np.mean(X, axis =0)
    X_c = X - mu
    mul = np.matmul(X_c.T, X_c)
    summ = ( 1/(X.shape[0]-1) ) * mul
    return summ