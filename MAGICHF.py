for _ in range(int(input())):
    n,x,s=[int(i) for i in input().split()]
    a=[0]*(n+1)
    a[x]=1
    for j in range(s):
        p,q=[int(i) for i in input().split()]
        a[p],a[q]=a[q],a[p]
    for i in range(n+1):
        if(a[i]==1):
            print(i)
