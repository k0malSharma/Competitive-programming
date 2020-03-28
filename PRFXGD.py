for _ in range(int(input())):
    s=input()
    k,x=[int(i) for i in input().split()]
    l=[0]*26
    p=0
    for i in s:
        l[ord(i)-97]+=1
        if (l[ord(i)-97]>x):
            if(k>0):
                l[ord(i)-97]-=1
                k-=1
                p-=1
            else:
                break;
        p+=1
    print(p)
