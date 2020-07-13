for _ in range(int(input())):
    n=int(input())
    ch=0 
    mt=0 
    for j in range(0,n):
        a,b=map(int,input().strip().split())
        m=0 
        n=0 
        while a>0:
            m+= a%10
            a=a//10
        while b>0:
            n+=b%10
            b=b//10
        if m>n:
            ch+=1 
        elif m<n:
            mt+=1 
        else:
            ch+=1 
            mt+=1 
    if ch>mt:
        print(0,ch)
    elif ch<mt:
        print(1,mt)
    else:
        print(2,ch)
    
