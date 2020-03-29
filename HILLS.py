for _ in range(int(input())):
    n,u,d=[int(i) for i in input().split()]
    h=[int(i) for i in input().split()]
    k=1
    p=1
    for i in range(n-1):
        if((h[i]+u)>=h[i+1] and h[i]<h[i+1]):
            k+=1
        elif((h[i]-d)<=h[i+1] and h[i]>h[i+1]):
            k+=1
        elif(h[i]==h[i+1]):
            k+=1
        elif(h[i]-d>h[i+1] and p==1):
            k+=1
            p-=1
        else:
            break;
    print(k)
