for _ in range(int(input())):
    a,b,n=[int(i) for i in input().split()]
    if(int(n%2)==1):
        a*=2
    print(int(max(a,b)//min(a,b)))
        
        
        
        
