for _ in range(int(input())):
    n,k=[int(i) for i in input().split()]
    a=[i for i in input().split()]
    for i in range(n-1,n-k-1,-1):
        if(a[i]=='H'):
            for j in range(i):
                if(a[j]=='H'):
                    a[j]='T'
                else:
                    a[j]='H'
    c=0
    for i in range(n-k):
        if(a[i]=='H'):
            c+=1
    print(c)
