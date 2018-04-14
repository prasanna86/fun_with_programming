'''Write a function to find the longest common 
prefix string among an array of strings. 
Example: 
Input : arr = ["abcbdbdb", "abcbdbeceee", "abd"] 
Output : "ab"
'''

'''
len(arr) = n
max len(arr[i]) = m for 1 <= i <= n
Shortest string in array (arr_s): len(arr_s) <= m
Longest common prefix: lcp <= s <= m
O(mn) algorithm
'''

def longestCommonPrefix(arr):
    shortest = min(arr, key=len)
    index = arr.index(shortest)
    arr.pop(index)
    n = len(arr)
    j = len(shortest)

    for i in range(n):
        cp_found = 0
        while(j > 0 and cp_found == 0):
            if(shortest[0:j] == (arr[i])[0:j]):
                lcp = shortest[0:j]
                cp_found = 1
            else:
                j = j-1
                if(j == 0):
                    lcp = None    
    return lcp

arr = [str(i) for i in input().split()]
#arr = ["abcbdbdb", "abcbdbeceee", "abd", "abcd"]
lcp = longestCommonPrefix(arr)
print(lcp)