# Homework 1: Optimal Stopping

### Group Members
    - Brandon Herrin (A02336477)
    - Josh Weeks (A02304519)

### Running
    - install requirements after creating your environment with "pip install -r requirements.txt"
    - run the Python script (e.g. `python3 HW1_Herrin_Brandon.py`)

## Part 1
1. The algorithm for determining the optimal threshold for stopping search of a list of numbers (expressed as a percentage of the list's length) is found in `HW1_Herrin_Brandon.py`. Running that Python script (e.g. `python3 HW1_Herrin_Brandon.py`) will determine the optimal threshold for stopping based on randomly-generated lists with uniform, normal (mean of 50, standard deviation of 10), and beta distributions (specifically Beta(2,7)).

2. The optimal stopping point for a randomly-generated list of uniform distribution was found to hover right around 37% (the stopping point fluctuates based upon the number of lists that are processed). This is in line with what we expect, given the mathematical proof we discussed in class.

## Part 2
1. Running `python3 HW1_Herrin_Brandon.py` also gives us an optimal stopping threshold for a normal distribution with a mean of 50 and a standard deviation of 10.

2. The standard distribution resulted on average in a higher optimal stopping threshold than the uniform distribution. 

3. Running `python3 HW1_Herrin_Brandon.py` also gives us an optimal stopping threshold for a beta distribution (Beta(2,7)).

## Part 3
1. Running `python3 HW1_Herrin_Brandon.py` gives us a best "search" threshold of 9-10% for a uniform distribution. After 10,000 simulations the average score after looking at that threshold was 80.25

2. Running `python3 HW1_Herrin_Brandon.py` gives us a threshold for the normal distribution that is slightly less than the uniform distribution, this time it is around 7%. After 10,000 simulations the average score after looking at that threshold was 56.66

3. There is a .png that is included in the repository that shows the results of the above two tests. It is titled: part_3_graph.png