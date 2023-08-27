from itertools import permutations

string,n=map(str,input().split())

output=list(permutations(string,int(n)))
output.sort()

for item in output:
    item=list(item)
    print("".join(item))
