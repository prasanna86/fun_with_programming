def sort_array(a):
    # Return a sorted array.
    n = len(a)
    odd = []
    index = []
    for i in range(n):
        if a[i]%2==1:
            index.append(i)
            odd.append(a[i])
    odd.sort()  # sorts in place
    for i in range(len(index)):
        a[index[i]] = odd[i]
    return a

def sort_array_simpler(arr):
  odds = sorted((x for x in arr if x%2 != 0), reverse=True)
  return [x if x%2==0 else odds.pop() for x in arr]

a = [9, -2, 3, 4, 2, 6, 8, 5]
b = sort_array(a)
print(b)