for _ in range(int(input())):
    n,k=[int(i) for i in input().split()]
    a=[int(i) for i in input().split()]
    r,p=0,-1
    for i in range(n):
        r+=a[i]
        r-=k
        if(r<0):
            p=i+1
            break
    if(p==-1):
        print("YES")
    else:
        print("NO ",p)
           
            
