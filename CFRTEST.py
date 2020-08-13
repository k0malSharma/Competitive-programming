for _ in range(int(input())):
    n=int(input())
    d=[int(i) for i in input().split()]
    a=[]
    for i in d:
        if i in a:
            continue
        else:
            a.append(i)
    print(len(a))
    
