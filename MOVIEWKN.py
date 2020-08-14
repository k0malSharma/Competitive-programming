for _ in range(int(input())):
    n=int(input())
    l=[int(i) for i in input().split()]
    r=[int(i) for i in input().split()]
    k=[]
    for i in range(n):
        k.append(l[i]*r[i])
    if (k.count(max(k))==1):
        print(k.index(max(k))+1)
    else:
        print(r.index(max(r))+1)
                
