import numpy as np
import matplotlib.pyplot as plt

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
num_trials = 10000

print(f"Optimal stopping point for uniform distribution: {test_optimal_stopping('uniform', stopping_point_range, num_trials)}")
print(f"Optimal stopping point for normal distribution: {test_optimal_stopping('normal', stopping_point_range, num_trials)}")
print(f"Optimal stopping point for beta distribution: {test_optimal_stopping('beta', stopping_point_range, num_trials)}")


def run_investment_decision(distribution, search_percentage):
    cutoff = int(len(distribution) * search_percentage)
    new_list = []
    for i in range(cutoff):
        new_list.append(distribution[i] - cutoff)

    return max(new_list)

def run_investment_test(num_trials, stopping_point_range, dist_function, norm):
    results = {}
    for threshold in stopping_point_range:
        score_list = []
        for i in range(num_trials):
            if norm == False:
                dist = dist_function(1, 99, 100)
            if norm == True:
                dist = dist_function(mean=50, std_dev=10, size=100, max_value=99)
            score_list.append(run_investment_decision(dist, threshold))
    
        results[threshold] = sum(score_list) / len(score_list)

    return results

stopping_point_range = np.arange(0.01, 0.60, 0.01)
num_trials = 10000

uniform_results = run_investment_test(num_trials, stopping_point_range, random_uniform_distribution, False)
normal_results = run_investment_test(num_trials, stopping_point_range, random_normal_distribution, True)

thresholds = list(uniform_results.keys())
uniform_scores = list(uniform_results.values())
normal_scores = list(normal_results.values())

plt.figure(figsize=(10, 6))

plt.plot(thresholds, uniform_scores, marker='o', linestyle='-', color='b', label='Uniform Distribution')
plt.plot(thresholds, normal_scores, marker='x', linestyle='--', color='r', label='Normal Distribution')

plt.xlabel('Threshold')
plt.ylabel('Average Score')
plt.title('Threshold vs. Average Score for Uniform and Normal Distributions')
plt.grid(True)
plt.legend()

plt.show()

best_uniform_threshold, best_uniform_score = max(uniform_results.items(), key=lambda x: x[1])
best_normal_threshold, best_normal_score = max(normal_results.items(), key=lambda x: x[1])

print(f"Best Uniform Distribution: Threshold = {best_uniform_threshold:.2f}, Average Score = {best_uniform_score:.2f}")
print(f"Best Normal Distribution: Threshold = {best_normal_threshold:.2f}, Average Score = {best_normal_score:.2f}")