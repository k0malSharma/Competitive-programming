for _ in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split()]
    b=[int(i) for i in input().split()]
    c=0
    for i in range(n):
        if(i==0):
            if(b[0]<=a[0]):
                c+=1
        else:
            if(b[i]<=a[i]-a[i-1]):
                c+=1
    print(c)
                
