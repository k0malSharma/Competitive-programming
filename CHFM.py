for _ in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split()]
    s=0
    k=0
    for i in a:
        s+=i
    for i in range(n):
        if(s/n==(s-a[i])/(n-1)):
            k=i+1
            break
    if(k==0):
        print("Impossible")
    else:
        print(k)
    
            
