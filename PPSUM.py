for _ in range(int(input())):
    d,n=[int(i) for i in input().split()]
    s=0
    for i in range(d):
        n=sum([j for j in range(1,n+1)])
    print(n)
