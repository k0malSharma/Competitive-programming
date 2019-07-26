for _ in range(int(input())):
    a=[int(i) for i in input().split()]
    x=min(a)
    y=max(a)
    for i in range(3):
        if(a[i]!=x and a[i]!=y):
            print(a[i])
    
