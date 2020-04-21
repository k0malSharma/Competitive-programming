for _ in range(int(input())):
    n=int(input())
    if(n==1):
        print(0)
    elif(n<4):
        print(1)
    else:
        e=[0,9,2,3]
        a=len(bin(n))-3
        s=a%4
        print(e[s])
    
