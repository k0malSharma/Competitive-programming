for _ in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split()]
    x,y,c=0,0,0
    for i in range(n):
        if(a[i]==0):
            x+=1
        if(a[i]==2):
            y+=1
    print(x*(x-1)//2+y*(y-1)//2)
