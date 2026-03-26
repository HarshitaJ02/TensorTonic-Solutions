import numpy as np

def global_avg_pool(x):
    """
    Compute global average pooling over spatial dims.
    Supports (C,H,W) => (C,) and (N,C,H,W) => (N,C).
    """
    # Write code here
    x = np.asarray(x, dtype = float)
    
    if x.ndim == 3:
        output = np.mean(x, axis = (1,2))
        
    elif x.ndim == 4:
        output = np.mean(x, axis = (2,3))
    else:
        raise ValueError("Array not of expected shape")
    return output
        
    