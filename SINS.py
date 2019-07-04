def gcd(x,y):
    if(x==0):
        return(y)
    return gcd(y%x,x)

    
for _ in range(int(input())):
    a, b = [int(i) for i in input().split()]
    c=gcd(a,b)
    print(2*c)
