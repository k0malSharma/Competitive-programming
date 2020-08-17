for _ in range(int(input())):
    h,p=[int(i) for i in input().split()]
    while(p>0 and h>0):
        h-=p
        p//=2
    if(h<=0):
        print("1")
    else:
        print("0")
        
