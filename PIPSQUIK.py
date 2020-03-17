for _ in range(int(input())):
    n,h,y1,y2,l=[int(i) for i in input().split()]
    t=[0]*n
    x=[0]*n
    for i in range(n):
        t[i],x[i]=[int(i) for i in input().split()]
    if(n<l):
        print(n)
    else:
        k=0
        for i in range(n):
            if (t[i]==1 and (h-y1)<=x[i]):
                k+=1
            elif (t[i]==2 and y2>=x[i]):
                k+=1
            else:
                l-=1
                if(l==0):
                    break
                k+=1
        print(k)
