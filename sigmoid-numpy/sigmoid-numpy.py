import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    x = np.array(x)
    denom = 1 + np.exp(-x)
    op =  1 / denom
    return op