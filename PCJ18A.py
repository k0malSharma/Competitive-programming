for _ in range(int(input())):
    n,x=[int(i) for i in input().split()]
    a=[int(i) for i in input().split()]
    k=0
    for i in range(n):
        if(a[i]>=x):
            k+=1
            break
    if(k==1):
        print("YES")
    else:
        print("NO")
