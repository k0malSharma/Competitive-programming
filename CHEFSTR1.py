import math
for _ in range(int(input())):
    n=int(input())
    s=[int(i)  for i in input().split()]
    p=0
    for i in range(n-1):
        p+=math.fabs(s[i+1]-s[i])-1
    print(int(p))
