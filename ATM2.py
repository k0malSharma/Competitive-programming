for _ in range(int(input())):
    n,k=[int(i) for i in input().split()]
    a=[int(i) for i in input().split()]
    s=""
    for i in range(n):
        if(k-a[i]>=0):
            k-=a[i]
            s+="1"
        else:
            s+="0"
    print(s)
