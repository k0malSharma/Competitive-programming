for _ in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split()]
    x,y,z=0,0,0
    c=0
    for i in a:
        if(i==5):
            x+=5
        elif(i==10):
            y+=10
            if(x-5<0):
                c=-1
                break
            else:
                x-=5
        else:
            z+=15
            if(y-10>=0):
                y-=10
            elif(x-10>=0):
                x-=10
            else:
                c=-1
                break
    if(c==-1):
        print("NO")
    else:
        print("YES")
 
