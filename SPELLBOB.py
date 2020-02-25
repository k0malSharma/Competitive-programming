for _ in range(int(input())):
    a=input()
    b=input()
    c=[0,0,0]
    bc=0
    oc=0
    for i in range(3):
        if(a[i]=='b' or b[i]=='b'):
            bc+=1
            c[i]+=1
        if(a[i]=='o' or b[i]=='o'):
            oc+=1
            c[i]+=1
    if all(i>=1 for i in c) and (bc>=2 and oc>=1):
        print("yes")
    else:
        print("no")
