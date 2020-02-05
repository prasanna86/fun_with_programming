```
P: Problem, S: Solution
P1, P2, ...., Pk are subproblems of P (of the same type but smaller size)
S1, S2, S3,...Sk are solutions to P1, P2,....Pk

Divide and conquer (recursive solution)
------------------
DAC(P)
{
    if(small(P))
    {
        S(P);
    }
    else
    {
        divide P into P1, P2,....Pk
        Apply DAC(P1), DAC(P2),...DAC(Pk)
        Combine(DAC(P1), DAC(P2), ...DAC(Pk))
    }
}

Examples:
1. Binary Search
2. Finding maximum and minimum
3. Merge Sort
4. Quick sort
5. Strassen's matrix multiplication