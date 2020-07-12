for _ in range(int(input())):
    n,b=[int(i) for i in input().split()]
    w,h,p=[0]*n,[0]*n,[0]*n
    for i in range(n):
        w[i],h[i],p[i]=[int(i) for i in input().split()]
    a=0
    for i in range(n):
        if(p[i]<=b and a<(w[i]*h[i])):
            a=w[i]*h[i]
    if(a==0):
        print("no tablet")
    else:
        print(a)
