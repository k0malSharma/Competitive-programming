n,k=[int(i) for i in input().split()]
s=[False]*n
a=[]
for i in range(k):
    x=input().split()
    if (len(x)==2):
        a.append(int(x[1]))
    else:
        a.append(-1)
for i in a:
    if(i==-1):
        s=[0]*n
    else:
        s[i-1]=not s[i-1]
    c=0
    for j in s:
        if(j==True):
            c+=1
    print(c)
