while(True):
    n=int(input())
    if(n==0):
        break
    a=[int(i) for i in input().split()]
    b=[0]*n
    k=1
    for i in a:
        b[i-1]=k
        k+=1
    if(a==b):
        print("ambiguous")
    else:
        print("not ambiguous")
