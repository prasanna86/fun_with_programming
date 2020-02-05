#!/bin/python3

import sys

def findMaxHourglassSum(arr):
    # Array size
    arr_size = len(arr)
    # Hourglass window size
    hg_win_size = 3
    # num_hg = (arr_size - hg_win_size + 1) ** 2 = 4 * 4 = 16
    num_hg_rows = (arr_size - hg_win_size + 1)
    # initialize hg_sum as empty array
    hg_sum = []
    # looping through array: since window size is 3, 
    # the loop starts at (3-1) / 2 = 1
    for i in range(1, num_hg_rows+1):
        for j in range(1,num_hg_rows+1):
            # summing 3 by 3 sub arrays 
            s = sum([sum(k[j-1:j+2]) for k in arr[i-1:i+2]])
            # subtracting 2 corner elements to get hourglass sum
            s -= (arr[i][j-1] + arr[i][j+1])
            # appending sum to list
            hg_sum.append(s)
    # returning max over all hourglass sums
    return max(hg_sum)

arr = []
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)

# find max hour glass sum
s = findMaxHourglassSum(arr)
print(s)