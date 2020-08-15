for _ in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split()]
    if(n==1):
        print("first")
    else:
        a.sort(reverse=True)
        p1=a[1]+sum(a[2::2])
        p2=sum(a)-p1
        if(p1<p2):
            print("first")
        elif(p1>p2):
            print("second")
        else:
            print("draw")
    
