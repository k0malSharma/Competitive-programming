for _ in range(int(input())):
    n=int(input())
    s=input()
    x,y=0,0
    for i in range(1,n,1):
        if(s[i]=='L' and s[i-1]!='L' and s[i-1]!='R'):
            x-=1
        elif(s[i]=='R' and s[i-1]!='L' and s[i-1]!='R'):
            x+=1
        elif(s[i]=='U' and s[i-1]!='U' and s[i-1]!='D'):
            y+=1
        elif(s[i]=='D' and s[i-1]!='U' and s[i-1]!='D'):
            y-=1
        else:
            continue
    if(s[0]=='L'):
        x-=1
    elif(s[0]=='R'):
        x+=1
    elif(s[0]=='U'):
        y+=1
    else:
        y-=1
    print(x," ",y)
