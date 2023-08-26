from itertools import product

A=list(map(int,input().split()))
B=list(map(int,input().split()))

output=list(product(A,B))

for item in output:
    print(item,"",end='')
