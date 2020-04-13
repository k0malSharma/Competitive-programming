for _ in range(int(input())):
    n=int(input())
    p=[0]*n
    s=[0]*n
    a=[0]*11
    add=0
    for i in range(n):
        p[i],s[i]=[int(j) for j in input().split()]
        if(a[p[i]-1]<s[i]):
            a[p[i]-1]=s[i]
    for i in range(8):
        add+=a[i]
    print(add)
        
        
