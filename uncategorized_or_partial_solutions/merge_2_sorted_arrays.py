def mergeBF(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
    if(m >= n):
        nums1.extend(nums2)
        nums1.sort()
    else:
        nums2.extend(nums1)
        nums2.sort()

def mergeLL(nums1, m, nums2, n):
    
    return m+n

a = [1, 4, 5, 8, 10]
b = [2, 3, 6, 7]
mergeBF(a,len(a), b, len(b))
print(a)

