for _ in range(int(input())):
    a=int(input())
    s=0
    while(a>0):
        s+=int(a%10)
        a=int(a/10)
    print(int(s))
    
