for _ in range(int(input())):
    p=int(input())
    a=[1,2,4,8,16,32,64,128,256,512,1024,2048]
    k=0
    n=0
    if p in a:
        print("1")
    else:
        while(p>0):
            while(k!=12 and a[k]<=p):
                k+=1
            n+=1
            p-=a[k-1]
            k=0
        print(n)       
