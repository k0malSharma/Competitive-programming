for _ in range(int(input())):
    s,n=[int(i) for i in input().split()]
    p=0
    if(s==1 or s%2!=0):
        p=1
        s-=1
    while(s>=2):
        p+=s//n
        s%=n
        n=s
    print(p)
