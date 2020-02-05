#!/bin/python3

import sys

# input integer
n = int(input().strip())

# convert to binary
b = bin(n)[2:]

# store max consecutive ones in list
max_ones = []
count = 0 # iterator

# scan through the binary string
for i in range(len(b)):
    if(b[i] == '1'):
        count += 1
    # iterate count until '0' hit & append
    else:
        max_ones.append(count)
        count = 0 # restart iterator
if(b[-1] == '1'):
    max_ones.append(count)
max_int = max(max_ones)
print(b, max_int)

