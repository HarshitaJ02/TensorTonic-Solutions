import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    # Write code here
    x = np.array(x)
    e_x = np.exp(x)
    e_minus_x = np.exp(-x)
    num = e_x - e_minus_x
    den = e_x + e_minus_x
    return num/den