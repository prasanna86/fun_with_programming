### Hackerrank: Greedy algorithms (Luck balance)
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    unimportant_contests_luck = [i[0] for i in contests if i[1] == 0]
    luck_from_losing_unimportant_contests = sum(unimportant_contests_luck) 

    important_contests_luck = [i[0] for i in contests if i[1] == 1]
    sorted_important_contests_luck = sorted(important_contests_luck, reverse=True)
    num_important = len(sorted_important_contests_luck)

    luck_balance = luck_from_losing_unimportant_contests
    for i in range(num_important):
        if(i <= k-1):
            luck_balance += sorted_important_contests_luck[i]
        else:
            luck_balance -= sorted_important_contests_luck[i]

    return luck_balance

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
