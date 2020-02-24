for _ in range(int(input())):
    q,p=[int(i) for i in input().split()]
    if(q>1000):
        pr=float((q*p)-((q*p)/10))
    else:
        pr=float(q*p)
    print("{0:.6f}".format(pr))
