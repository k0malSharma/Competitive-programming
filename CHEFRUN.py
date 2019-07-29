for _ in range(int(input())):
    x1,x2,x3,v1,v2=[int(i) for i in input().split()]
    d1=x3-x1
    d2=x2-x3
    t1=d1/v1
    t2=d2/v2
    if t1<t2:
        print("Chef")
    elif t1>t2:
        print("Kefa")
    else:
        print("Draw")
     
