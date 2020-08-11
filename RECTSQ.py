import math
for _ in range(int(input())):
    l,b=[int(i) for i in input().split()]
    x=math.gcd(l,b)
    print((l//x)*(b//x))
