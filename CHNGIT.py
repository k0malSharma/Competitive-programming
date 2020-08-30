for _ in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split()]
    c=0
    for i in set(a):
        if(c<a.count(i)):
            c=a.count(i)
    print(len(a)-c)
        
