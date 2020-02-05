## Hackerrank: Greedy algorithms --- Greedy florist

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    cost = 0
    ## Sorting pricing of flowers in ascending order
    sorted_c = sorted(c)

    for i in range(k):
        ## The flowers assigned for Friend i to buy
        subarray_c = sorted_c[i::k]
        m = len(subarray_c)
        ## Friend i will buy his assigned flowers in
        # descending order of price to minimize his cost
        cost += sum([(m-i) * subarray_c[i] for i in range(m)])

    return cost
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
