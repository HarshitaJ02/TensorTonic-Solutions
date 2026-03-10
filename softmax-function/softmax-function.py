import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    # Write code here
    x = np.atleast_2d(x).astype(float)    
    e = np.exp(x- np.max(x, axis =1, keepdims = True)) 
    s = e/np.sum(e, axis= 1, keepdims = True)

    return s if x.shape[0]>1 else s[0]
    