n=int(input())
c=[int(i) for i in input().split()]
t=[int(i) for i in input().split()]
p=100001
x,y=100001,100001
for i in range(n):
    if(t[i]==3):
        if(c[i]<p):
            p=c[i]
    else:
        if(t[i]==1):
            if(c[i]<x):
                x=c[i]
        else:
            if(c[i]<y):
                y=c[i]
if(p<=x+y):
    print(p)
else:
    print(x+y)
