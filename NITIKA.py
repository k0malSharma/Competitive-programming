for t in range(int(input())):
    s=[str(i) for i in input().split()]
    n=len(s)-1
    for i in range(n):
        st=str(s[i][:1]).upper()
        print(st,end=". ")
    st=str(s[n][:1]).upper()+str(s[n][1:]).lower()
    print(st)
    
