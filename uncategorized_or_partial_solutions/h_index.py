# find a researcher's h-index
# h-index: The largest number of papers h that have atleast h citations
# Input: Papers(A, B, C, D, E) and Citations (2, 4, 1, 8, 7)
# Output: 3 (corresponding to B, D, E)

# How to think about this?
# Given an array of n elements, Are there atleast h elements greater than or equal to h?

# Questions
# Can I assume array is non-empty?
# Can I assume each array element is non-negative? ( >= 0 )



def find_h_index_brute(arr):
    if(sum(arr) == 0): # assuming array has no negative elements
        return 0
    
    h = 1
    # check if there's 1 element greater than 1
    i = 0
    while(i < range(len(arr) and count == 0):
        if arr[i] >= h:
            count = count + 1
        i = i + 1
    if i == len(arr)
