for _ in range(int(input())):
    n=int(input())
    s=input()
    flag=0
    for i in range(n):
        if ((s[i]!='a' and s[i]!='e' and s[i]!='i' and s[i]!='o' and s[i]!='u') and i <= len(s)-2):
            if (s[i+1]=='a' or s[i+1]=='e' or s[i+1]=='i' or s[i+1]=='o' or s[i+1]=='u'):
                flag+=1
    print(flag)    
                
        
