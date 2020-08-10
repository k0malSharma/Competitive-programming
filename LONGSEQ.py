for _ in range(int(input())):
    n=input()
    a=[0,0]
    for i in n:
        if(i=='0'):
            a[0]+=1
        else:
            a[1]+=1
        if(a[0]>=2 and a[1]>=2):
            break
    if(a[0]==1 or a[1]==1):
        print("Yes")
    else:
        print("No")
