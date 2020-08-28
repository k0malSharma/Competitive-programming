for _ in range(int(input())):
    n,k=[int(i) for i in input().split()]
    p=[int(i) for i in input().split()]
    rev=sum(p)
    amt=0
    for i in p:
        if(i>k):
            amt+=k
        else:
            amt+=i
    print(rev-amt)
