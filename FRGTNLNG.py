for _ in range(int(input())):
    n,k=[int(i) for i in input().split()]
    s=input().split()
    a,m=[],[0]*n
    for i in range(k):
        a=input().split()
        for j in range(n):
            if s[j] in a:
                m[j]=1
    for i in m:
        if(i==1):
            print("YES",end=' '),
        else:
            print("NO",end=' '),
    print(end='\n')
