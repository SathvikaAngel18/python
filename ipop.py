n = int(input())
a=list(map(int,input().strip('[]').split(',')))[:n]
for i in a: 
    if a.count(i) > 1:
       a.remove(i)
    sorted(a)
print(a)
