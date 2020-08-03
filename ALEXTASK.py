def gcd(a,b): 
    if a == 0: 
        return b 
    return gcd(b % a, a) 
  
def lcm(a,b): 
    return (a*b) // gcd(a,b)

for _ in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split()]
    a.sort()
    s=[]
    for i in range(n):
        for j in range(i+1,n):
            s.append(lcm(a[i],a[j]))
    print(min(s))
        
