import numpy as np
def id_gen():
    rng=np.random.default_rng()
    return rng.integers(10000,99999)