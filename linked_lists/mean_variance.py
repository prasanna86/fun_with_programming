import math
from typing import Iterator

# Given a stream of values in the form of an iterator, compute the mean
# and variance

# sample mean = \sum_i x_i / n
# sample variance = \sum_i (x_i - mean)^2 / (n - 1) = 1/(n-1) * \sum_i (x_i^2) - (n / n-1) * mean ** 2

def get_mean_and_variance(items: Iterator[float]):
    
    mean, variance = None, None
    if items.value is not None:
        mean, variance = items.value, 0
        count_values = 1
    
        while items.get_next() is not None:
            items = items.get_next()
            count_values += 1
            variance = ((count_values-2) * variance + (items.value - mean) ** 2) / (count_values-1) 
            mean = ((count_values-1) * mean + items.value) / count_values 
    
    return dict({'mean': mean, 'variance': variance})
