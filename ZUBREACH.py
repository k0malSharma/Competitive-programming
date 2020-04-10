for t in range(int(input())):
    m,n=[int(i) for i in input().split()]
    rx,ry=[int(i) for i in input().split()]
    l=int(input())
    s=input()
    l,u,d,r=0,0,0,0
    for i in s:
        if(i=='L'):
            l+=1
        elif(i=='U'):
            u+=1
        elif(i=='R'):
            r+=1
        else:
            d+=1
    x=r-l
    y=u-d
    print("Case",t+1,end="")
    if(x==rx and y==ry):
        print(": REACHED")
    elif(x<0 or x>m or y<0 or y>n):
        print(": DANGER")
    else:
        print(": SOMEWHERE")
