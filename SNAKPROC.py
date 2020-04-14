for _ in range(int(input())):
    n=int(input())
    s=input()
    h,t=0,0
    for i in s:
        if(i=='H'):
            h+=1
        if(i=='T'):
            t+=1
    if(t!=h):
        print("Invalid")
    else:
        k,p=0,0
        
        for i in s:
            if(i=='H'):
                k+=1
            if(i=='T'):
                k-=1
            if(k>1 or k<0):
                p=1
                break
        if(p==1):
            print("Invalid")
        else:
            print("Valid")
 
