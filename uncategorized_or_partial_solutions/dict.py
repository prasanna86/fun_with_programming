n = int(input())
a = list()
for i in range(n):
    key_value = input().strip().split()
    a.append(key_value)

d = dict(a)
for i in range(n):
    key = str(input())
    if(key in d):
        print(key,d[key],sep="=")
    else:
        print("Not found")

