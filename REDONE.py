m=10**9+7
z=10**6+1
l=[0]*z
l[1]=1
x=1
for i in range(2,z):
    x=(x+i+(x*i))%m
    l[i]=x
for _ in range(int(input())):
    n=int(input())
    print(l[n])
