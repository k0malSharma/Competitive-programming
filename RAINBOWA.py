for _ in range(int(input())):
    n=int(input())
    k=n-1
    flag=0
    a=[int(i) for i in input().split()]
    s=[1,2,3,4,5,6,7]
    st=list(set(a))
    print(s," ",st)
    if(s==st):
        for i in range(n//2):
            print(a[i]," ",a[k])
            if(a[i]!=a[k]):
                flag=1
                break; 
            k-=1
        if(flag==0):
             print("yes")
        else:
            print("no")
    else:
        print("no")
