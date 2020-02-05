"""
returns list
example invocation
take_weighted_sample(10, ["Heads", "Tails"], [0.5, 0.5]) =  ["Heads","Heads","Tails","Heads","Heads","Tails","Tails","Heads","Tails","Heads",]

# I was re-evaluating my code for syntax correctness and made changes so that it runs as expected on command line
* changed range(weights) to range(len(weights))
* added a break command on line 25
* checked the iterator for sum of weights to go to i+1
* cleaned up as 2 functions
* using "random" library for uniform random numbers
"""
import random
def sum_of_weights(weights):
    sum_weights = []
    for i in range(len(weights)):
        sum_weights.append(sum(weights[0:i+1]))
    return sum_weights

def take_weighted_sample(num_samples, classes, weights):
    sum_weights = sum_of_weights(weights)
    sample = []
    for i in range(num_samples):
        u = random.uniform(0, 1)
        for i in range(len(sum_weights)):
            if(u <= sum_weights[i]):
                sample.append(classes[i])
                break
            else:
                continue
    return sample

sum_weights = sum_of_weights([0.5,0.5])
print(sum_weights)

sample = take_weighted_sample(10, ["Heads", "Tails"], [0.5, 0.5])
print(sample)