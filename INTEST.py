a, b = [int(i) for i in input().split()]
c=0
for i in range(a):
    d=int(input())
    if d%b==0:
        c+=1
print(c)       
