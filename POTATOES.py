def isprime(n):
    if n==1:
        return False
    else:
        for i in range(2,(n//2)+1):
            if n%i == 0:
                return False
        else:
            return True
for _ in range(int(input())):
    x,y=[int(i) for i in input().split()]
    s= x+y+1 
    while (isprime(s)==False):
        s+=1     
    print(s-(x+y))
