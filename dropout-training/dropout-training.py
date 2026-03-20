import numpy as np

def dropout(x, p=0.5, rng=None):
    """
    Apply dropout to input x with probability p.
    Return (output, dropout_pattern).
    """
    # Write code here
    x = np.asarray(x,dtype = float)
    if rng:
        random_arr = rng.random(x.shape)
    else:
        random_arr = np.random.rand(*x.shape)

    mask = random_arr < 1-p
    pattern = mask * (1/(1-p))
    output = x * pattern
    return (output, pattern)
    
    