import math
for _ in range(int(input())):
    r=int(input())
    c=[int(i) for i in input().split()]
    hs=[int(i) for i in input().split()]
    sc=[int(i) for i in input().split()]
    d1=math.sqrt(math.pow(c[0]-hs[0],2)+math.pow(c[1]-hs[1],2))
    d2=math.sqrt(math.pow(c[0]-sc[0],2)+math.pow(c[1]-sc[1],2))
    d3=math.sqrt(math.pow(sc[0]-hs[0],2)+math.pow(sc[1]-hs[1],2))
    if(d1<=r and d2<=r):
        print("yes")
    elif((d1<=r or d2<=r) and d3<=r):
        print("yes")
    else:
        print("no")
