n=int(input())
a=[int(i) for i in input().split()]
b=list(set(a))
if(len(b)==1):
    print(0)
else:
    b.sort()
    print(b[-2])
