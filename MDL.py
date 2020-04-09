for _ in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split()]
    b=[int(i) for i in a]
    a.sort(reverse=True)
    for i in b:
        if(i==a[0] or i==a[n-1]):
            print(i,end=" ")
    print("\n",end="")
