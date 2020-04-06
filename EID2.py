for _ in range(int(input())):
    a1,a2,a3,c1,c2,c3=[int(i) for i in input().split()]
    c=[c1,c2,c3]
    d=[c1,c2,c3]
    a=[a1,a2,a3]
    k=0
    for i in range(2):
        for j in range(i+1,3):
            if(a[i]>a[j]):
                a[i],a[j]=a[j],a[i]
                c[i],c[j]=c[j],c[i]
            if((a[i]==a[j] and c[i]!=c[j]) or(a[i]!=a[j] and c[i]==c[j])):
                k+=1;
                break;
    d.sort()
    if(k==0 and c==d):
        print("FAIR")
    else:
        print("NOT FAIR")

