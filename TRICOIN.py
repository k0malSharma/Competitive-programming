for _ in range(int(input())):
    n=int(input())
    s,i=0,1
    while(s<=n):
        s+=i
        i+=1
    print(i-2)
