for _ in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split()]
    a.sort(reverse= True)
    print(a[n-1])
