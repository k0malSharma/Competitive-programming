for _ in range(int(input())):
    n=int(input())
    p=[]
    for i in range(n):
        p.append([int(i) for i in input().split()])
    s=0
    for i in range(1,n+1):
        s^=i
    print(s)
