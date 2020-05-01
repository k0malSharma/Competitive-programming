for _ in range(int(input())):
    s=input()
    if(len(s)==1 or len(s)==2):
        print("YES")
    else:
        v=""
        for i in range(2,len(s)):
            v+=s[i]
        v+=s[0]+s[1]
        if(v==s):
            print("YES")
        else:
            print("NO")
    
        
