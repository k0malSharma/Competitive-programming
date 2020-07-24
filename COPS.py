for _ in range(int(input())):
    m,x,y=[int(i) for i in input().split()]
    a=[int(i) for i in input().split()]
    d=x*y
    s=[0]*100
    for i in a:
        p=i-d
        q=i+d
        if p<1:
            p=1
        if q>100:
            q=100
        for j in range(p-1,q):
            s[j]=1
    print(s.count(0))
