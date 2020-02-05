def construct_dataset(x, f):
    n = len(x)
    s = []
    for i in range(n):
        for j in range(f[i]):
            s.append(x[i])
    s = sorted(s)
    return s


def median(x):
    sz = len(x)
    if sz % 2 != 0:
        return x[sz // 2]
    else:
        return (x[sz // 2] + x[sz // 2 - 1]) / 2


def inter_quartile_range(x, f):
    sz = sum(f)
    # construct and output a sorted dataset
    s = construct_dataset(x, f)
    # separate left and right parts of dataset
    sleft = [int(i) for i in s[0:sz // 2]]
    if (sz % 2 == 0):
        sright = [int(i) for i in s[(sz // 2):sz]]
    else:
        sright = [int(i) for i in s[(sz // 2) + 1:sz]]
    # compute lower and upper quartiles
    q1 = median(sleft)
    q3 = median(sright)
    # compute inter quartile range
    iqr = q3 - q1
    return iqr


n = int(input())
x = [int(i) for i in input().split()]
f = [int(i) for i in input().split()]

iqr = inter_quartile_range(x, f)
print(round(iqr, 1))
