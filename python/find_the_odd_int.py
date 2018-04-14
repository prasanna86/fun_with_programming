from collections import Counter

def find_it(seq):
    freqs = Counter(seq)
    a = freqs.most_common()
    i = 0
    while(i < len(a)):
        if(a[i][1]%2 == 1):
            return a[i][0]
        else:
            i = i+1
    s = "No odd frequencied element in this sequence. try something else!"
    return s

def find_it_simpler(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i

element = find_it_simpler([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])
print(element)
