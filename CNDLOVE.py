for _ in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split()]
    b=0
    for i in range(n):
        b=b+a[i]
    if(b%2==0):
        print("NO")
    else:
        print("YES")
