for _ in range(int(input())):
    n=int(input())
    s=[""]*n
    for i in range(n):
        s[i]=input()
    c=[0]*26
    for i in s:
        for j in i:
            c[ord(j)-97]+=1
    m=[c[2]//2,c[14],c[3],c[4]//2,c[7],c[5]]
    print(min(m))
