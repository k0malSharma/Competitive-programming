for _ in range(int(input())):
    s=input()
    st=""
    c=1
    for i in range(len(s)-1):
        if(s[i]==s[i+1]):
            c+=1
        else:
            st+=s[i]+str(c)
            c=1
    st+=s[len(s)-1]+str(c)
    if(len(st)<len(s)):
        print("YES")
    else:
        print("NO")
