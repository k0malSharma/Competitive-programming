for _ in range(int(input())):
    n=int(input())
    s=input()
    u=input()
    if s==u:
        print(n)
    else:
        k=0
        flag=0
        for i in range(n-1):
            if(s[i]==u[i] and flag==0):
                k+=1
            elif(u[i]=='N' and flag==0):
                k+=0
            elif(u[i]!=s[i] and flag==0):
                flag+=1
            else:
                flag=0
        if(flag==0 and s[n-1]==u[n-1]):
            k+=1
        print(k)
        
