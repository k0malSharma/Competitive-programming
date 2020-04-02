for _ in range(int(input())):
    n=int(input())
    amt=0
    p,q,d,m,l=[0]*n,[0]*n,[0]*n,[0]*n,[0]*n
    for i in range(n):
        p[i],q[i],d[i]=[int(i) for i in input().split()]
        m[i]=p[i]+((d[i]/100)*p[i])
        l[i]=m[i]-((d[i]/100)*m[i])
        amt+=(p[i]-l[i])*q[i]
    print('{0:.5f}'.format(amt))
