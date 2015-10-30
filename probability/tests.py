# trying out a few basic probably calculations
from collections import Counter

sample_set = [1,2,5,7,3,5,6,7,6,3,4,5,3,4,7,6,2,6,5,2,7,8,3,5,7,0,1,3,6,8,3,6,4,5]

Counter(sample_set)

def quantile(x, p):
    p_index = int(p * len(x))
    return sorted(x)[p_index]

# print quantile(sample_set, .80)
# print quantile(sample_set, .95)
# print quantile(sample_set, .1)


def mean(x):
    return sum(x) / len(x)

def sum_of_squares(x):
    sum = 0
    x_bar = mean(x)
    for x_i in x:
        sum += (x_i - x_bar)**2
    return sum

def de_mean(x):
    x_bar = mean(x)
    return[x_i - x_bar for x_i in x]

### todo: still problems with this.

def variance(x):
    n = len(x)
    deviations = de_mean(x)
    return float(sum_of_squares(x)) / (n - 1)

print sum_of_squares(sample_set)
print variance(sample_set)

from numpy import var
print var(sample_set)

# variance, covariance, stddev, correllation
