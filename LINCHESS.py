for _ in range(int(input())):
    n,k=[int(i) for i in input().split()]
    p=[int(i) for i in input().split()]
    a=[]
    for i in p:
        if(k%i==0):
            a.append(i)
    if(len(a)==0):
        print(-1)
    else:
        print(max(a))
