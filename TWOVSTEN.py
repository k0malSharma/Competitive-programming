for _ in range(int(input())):
    x=int(input())
    if(x%5==0 or x%10==0):
        k=0
        while(x%10!=0):
            x*=2
            k+=1
        print(k)
    else:
        print("-1")
