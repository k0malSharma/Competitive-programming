import math
for _ in range(int(input())):
    p=[int(i) for i in input().split()]
    n=p.pop(0)
    a=p[0]
    for i in range(1,n):
        a=math.gcd(a,p[i])
    for i in range(n):
        print(p[i]//a,end=" ")
    print()
