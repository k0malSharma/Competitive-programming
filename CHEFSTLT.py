for _ in range(int(input())):
    s1=input()
    s2=input()
    mn,mx=0,len(s1)
    for i in range(len(s1)):
        if(s1[i]==s2[i] and s1[i]!='?'):
            mx-=1
        if(s1[i]!=s2[i] and s1[i]!='?' and s2[i]!='?'):
            mn+=1      
    print(mn,mx)
