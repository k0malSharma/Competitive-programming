for _ in range(int(input())):
    n,k,e,m=[int(i) for i in input().split()]
    a=[0]*(n)
    b=[0]*e
    for i in range(n):
        b[e-1]=0
        b=[int(i) for i in input().split()]
        a[i]=sum(b)
    p=a[n-1]
    a.sort(reverse=True)
    q=a[k-1]
    if(q-p+1<=m and q-p+1>0):
        print(q-p+1)
    elif(q-p+1<=0):
        print("0")
    else:
        print("Impossible")
