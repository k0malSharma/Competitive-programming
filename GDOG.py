for _ in range(int(input())):
    n,k=[int(i) for i in input().split()]
    m,r=0,1
    for i in range(2,k+1):
        if(n%i>m):
            m=n%i
    print(m)
