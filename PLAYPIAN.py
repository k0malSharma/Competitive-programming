for _ in range(int(input())):
    s=input()
    n=len(s)//2
    a=list()
    p=0
    k=2
    flag=0
    for i in range(n):
        a.append(s[p:k])
        k+=2
        p+=2
    for i in range(n):
        if ("AB"!=a[i] and "BA"!=a[i]):
            flag+=1
            break
    if(flag==0):
        print("yes")
    else:
        print("no")
    
        
