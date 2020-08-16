for _ in range(int(input())):
    c,d,l=[int(i) for i in input().split()]
    if(l%4!=0 or l<(d*4)):
        print("no")
    else:
        m=0
        l//=4
        if(c>d*2):
            m=c-d
        else:
            m=d
        if(m<=l and l<=(c+d)):
           print("yes")
        else:
           print("no")
