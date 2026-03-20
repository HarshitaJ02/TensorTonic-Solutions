import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    x = np.asarray(x, dtype = float)
    max_cal = np.max(x, axis =-1, keepdims = True)
    numero = np.exp(x - max_cal)
    summ = np.sum(numero, axis = -1, keepdims = True)
    return numero / summ
    