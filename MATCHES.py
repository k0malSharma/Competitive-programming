s=[6,2,5,5,4,5,6,3,7,6]
for _ in range(int(input())):
    a,b=[int(i) for i in input().split()]
    n=a+b
    p,d=0,0
    while(n>0):
        d=n%10
        p+=s[d]
        n//=10
    print(p)
    
