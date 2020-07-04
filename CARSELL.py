for _ in range(int(input())):
    n=int(input())
    p=[int(i) for i in input().split()]
    mod=(10**9)+7
    s=0
    p.sort(reverse=True)
    for i in range(n):
        if((p[i]-i)>0):
            s+=p[i]-i
    print(s%mod)
        
