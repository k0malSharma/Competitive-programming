for _ in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split()]
    c,o=0,0
    for i in a:
        if(i%2!=0):
            o+=1
    i=0
    while(i<n):
        if(a[i]%2!=0):
            o-=1
        else:
            c+=o
        i+=1
    print(c)
