import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    # Write code here
    x = np.asarray(x, dtype=float)
    if x.ndim ==1:
        fn = np.exp(x - max(x))
        fn2 = np.sum(fn)
        return fn/fn2
    else:
        fn = np.exp(x- np.max(x, axis =1, keepdims = True)) 
        summation = np.sum(fn, axis= 1, keepdims = True)
        return fn/summation
    