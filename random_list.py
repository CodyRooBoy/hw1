import numpy as np

def random_uniform_distribution(low=0, high=1000, size=1000):
    return np.random.uniform(low, high, size)

def random_normal_distribution(mean=0.0, std_dev=1.0, size=1000, max_value=None):
    dist = np.random.normal(mean, std_dev, size)
    if max_value is not None:
        dist = np.clip(dist, a_min=None, a_max=max_value)
    
    return dist

def random_beta_distribution(a, b, size=1000):
    return np.random.beta(a, b, size)