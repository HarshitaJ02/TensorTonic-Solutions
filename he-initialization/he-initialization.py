def he_initialization(W, fan_in):
    """
    Scale raw weights to He uniform initialization.
    """
    W = np.asarray(W, dtype= float)
    limit = np.sqrt(6/fan_in)
    return W * (2*limit) - limit
    