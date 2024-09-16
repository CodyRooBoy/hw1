import numpy as np

from random_list import random_uniform_distribution, random_normal_distribution, random_beta_distribution

def evaluate_stopping_point(list, stopping_point):
    max_value = max(list)
    n = len(list)
    m = int(np.floor(stopping_point * n))
    
    observed_segment = list[:m]
    max_observed = max(observed_segment)
    
    if max_value == max_observed:
        return False
    else:
        for i in range(m, n):
            if list[i] > max_observed and list[i] == max_value:
                return True
            elif list[i] > max_observed and list[i] != max_value:
                return False
        return False

def test_optimal_stopping(distribution_type, stopping_point_range, num_trials):
    true_counts = {stopping_point: 0 for stopping_point in stopping_point_range}

    for _ in range(num_trials):
        if distribution_type == 'uniform':
            random_list = random_uniform_distribution(0, 1000, 1000)
        elif distribution_type == 'normal':
            random_list = random_normal_distribution(50, 10, 1000)
        elif distribution_type == 'beta':
            random_list = random_beta_distribution(2, 7, 1000)

        for stopping_point in stopping_point_range:
            result = evaluate_stopping_point(random_list, stopping_point)
            if result:
                true_counts[stopping_point] += 1

    optimal_stopping_point = max(true_counts, key=true_counts.get)

    return optimal_stopping_point

stopping_point_range = np.arange(0.1, 0.60, 0.01)
num_trials = 1000

print(f"Optimal stopping point for uniform distribution: {test_optimal_stopping('uniform', stopping_point_range, num_trials)}")
print(f"Optimal stopping point for normal distribution: {test_optimal_stopping('normal', stopping_point_range, num_trials)}")
print(f"Optimal stopping point for beta distribution: {test_optimal_stopping('beta', stopping_point_range, num_trials)}")