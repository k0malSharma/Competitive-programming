import math
for _ in range(int(input())):
    n=int(input())
    c,s=0,0
    while(n>0):
        s=math.floor(math.sqrt(n))
        n-=s*s
        c+=1
    print(c)  
