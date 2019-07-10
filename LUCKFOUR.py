for _ in range(int(input())):
    count =0
    n=int(input())
    while(n>0):
        d=int(n%10)
        if(d==4):
            count+=1
        n=n//10
    print(count)
    
