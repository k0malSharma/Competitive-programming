import math
for _ in range(int(input())):
    n,v1,v2=[int(i) for i in input().split()]
    d1=2*n
    d2=math.sqrt(2)*n
    e=d1/v2
    s=d2/v1
    if(e>s):
        print("Stairs")
    else:
        print("Elevator")
    
