import math
t=int(input())
while(t!=0):
    n,a,k=map(int,input().split())
    q=n*(n-1)
    p=(((n-2)*360-(2*a*n))*(k-1))+(a*q)
    x=math.gcd(p,n*(n-1))
    print(int(p/x), int(q/x))
    t=t-1
