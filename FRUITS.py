for _ in range(int(input())):
    n,m,k=[int(i) for i in input().split()]
    diff=0
    if n<m:
        m,n=n,m
    m+=k
    if(n-m<=0):
        print(0)
    else:
        print(n-m)
