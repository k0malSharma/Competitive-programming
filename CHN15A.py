for _ in range(int(input())):
    n,k=[int(i) for i in input().split()]
    s=[int(i) for i in input().split()]
    c=0
    for i in s:
        if((i+k)%7==0):
            c+=1
    print(c)
