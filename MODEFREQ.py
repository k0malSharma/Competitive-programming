for _ in range(int(input())):
    n=[int(i) for i in input().split()]
    a=[int(i) for i in input().split()]
    a.sort()
    b=list(dict.fromkeys(a))
    c=[0]*len(b)
    for i in range(len(b)):
        c[i]=a.count(b[i])
    c.sort()
    d=list(dict.fromkeys(c))
    e=[]
    for i in range(len(d)):
        e.append(c.count(d[i]))
    m=e.index(max(e))
    print(d[m])
