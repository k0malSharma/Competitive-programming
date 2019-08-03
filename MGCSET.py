import math
for _ in range(int(input())):
    n,m=[int(i) for i in input().split()]
    a=[int(i) for i in input().split()]
    k=0
    for i in a:
        if (int(i%m)==0):
            k+=1
    print(int(math.pow(2,k)-1))
