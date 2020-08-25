for _ in range(int(input())):
    n,k=[int(i) for i in input().split()]
    w=[int(i) for i in input().split()]
    p,s=1,0
    i=0
    while(i<n):
        s+=w[i]
        if(s>k):
            s=w[i]
            p+=1
        if(w[i]>k):
            p=-1
            break
        i+=1
    print(p)
