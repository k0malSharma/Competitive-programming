for _ in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split()]
    for i in a:
        if(i%2==0):
            print("NO")
            n=-1
            break
    if(n!=-1):
        print("YES")
