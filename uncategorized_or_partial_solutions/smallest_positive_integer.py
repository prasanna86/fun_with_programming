
def solution(A):
    n = len(A)
    # using swaps, lets compare iterator+1 and 
    # the actual integer at that place
    for i in range(n):
        t = A[i]
        while(t < n and t != A[t]):
            newt = A[t]
            A[t] = t
            t = newt
    for i in range(n):
        if(A[i] != i+1):  
            return i+1
    return n
    
A = [1, 2, 3, 5, 5, 5, 6]
result = solution(A)
print(result)