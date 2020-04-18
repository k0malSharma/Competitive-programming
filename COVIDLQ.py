for _ in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split()]
    b=True
    for i in range(n):
        if a[i]==1:
            c=i
            break
    for i in range(c+1,n):
        if a[i]==1:
            if i-c<6:
                b=False
                break
            else:
                c=i
    if b:
        print("YES")
    else:
        print("NO")
