n,k=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]
mod=mod = (10**9)+7
p = [[a[0],0]]
for i in range(1,n):
    while p[0][1] + k < i:
        p.pop(0)
    temp = p[0][0]*a[i]
    while p[-1][0]>temp and len(p) != 1:
        p.pop(-1)
    p.append([temp,i])
print(p[-1][0]%mod)
        
