for _ in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split()]
    b=[]
    c=0
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            b.append([i,j])
   
    for i in range(len(b)):
        x=b[i][0]
        y=b[i][1]
        if a[x-1]&a[y-1]==a[x-1]:
            c=c+1
    print(c)
