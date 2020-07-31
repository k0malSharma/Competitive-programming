for _ in range(int(input())):
    s=input()
    a=[0]*26
    b=[0]*26
    for i in range(0,len(s)//2):
        a[ord(s[i])-97]+=1
    if(len(s)%2==0):
        for i in range(len(s)//2,len(s)):
            b[ord(s[i])-97]+=1
    else:
        for i in range(len(s)//2+1,len(s)):
            b[ord(s[i])-97]+=1
    if(a==b):
        print("YES")
    else:
        print("NO")
        
    
