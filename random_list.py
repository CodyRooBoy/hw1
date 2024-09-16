import numpy as np

def random_uniform_distribution(low=0, high=1000, size=1000):
    return np.random.uniform(low, high, size)

def random_normal_distribution(mean=0.0, std_dev=1.0, size=1000):
    return np.random.normal(mean, std_dev, size)

def random_beta_distribution(a, b, size=1000):
    return np.random.beta(a, b, size)