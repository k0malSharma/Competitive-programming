for _ in range(int(input())):
    n=int(input())
    a,p=[],n-1
    for i in range(n):
        a.append(int(input()))
    a.sort()
    for i in range(0,n-1,2):
        if(a[i]!=a[i+1]):
            p=i
            break;
    print(a[p])
