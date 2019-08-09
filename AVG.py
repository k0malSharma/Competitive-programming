for _ in range(int(input())):
    n,k,v=[int(i) for i in input().split()]
    a=[int(i) for i in input().split()]
    x=(v*(n+k))-sum(a)
    if (x%k==0 and x/k>0):
        print(x//k)
    else:
        print("-1")
