for _ in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split()]
    a.sort()
    k=0
    for i in range(n-1):
        if(a[i]==a[i+1]):
            k+=1
            break
    if(k==1):
        print("Yes")
    else:
        print("No")
