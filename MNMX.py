for _ in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split()]
    a.sort()
    print(a[0]*(n-1))
