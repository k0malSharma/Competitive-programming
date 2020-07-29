def gcd(a,b):
    while b > 0:
        a, b = b, a % b
    return a
    
def lcm(a, b):
    return a * b / gcd(a, b)

for _ in range(int(input())):
    n,a,b,k=[int(i) for i in input().split()]
    x,y,z=0,0,0
    p=lcm(a,b)
    x=n//a
    y=n//b
    z=n//p
    if(x+y-(2*z)>=k):
        print("Win")
    else:
        print("Lose")
