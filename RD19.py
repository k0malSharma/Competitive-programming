import math
for _ in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split()]
    p=a[0]
    for i in range(n):
        p=math.gcd(p,a[i])
    if(p==1):
        print(0)
    else:
        print(-1)
    
