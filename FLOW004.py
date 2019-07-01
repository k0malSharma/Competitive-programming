for _ in range(int(input())):
    n=int(input())
    s=int(n%10)
    t=0
    while (n>0):
        t=int(n%10)
        n=int(n/10)
    s=s+t
    print(s)
