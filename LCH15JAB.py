for _ in range(int(input())):
    s=input()
    a=[0]*26
    for i in s:
        a[ord(i)-97]+=1
    a.sort(reverse=True)
    i=1
    m=0
    while(a[i]!=0):
        m+=a[i]
        i+=1
    if(m==a[0]):
        print("YES")
    else:
        print("NO")
