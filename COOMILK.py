for _ in range(int(input())):
    n=int(input())
    s=input().split()
    flag=0
    for i in range(n):
        if(s[0]=="cookie" and n==1):
            flag+=1
            break
        if(s[n-1]=="cookie"):
            flag+=1
            break
        if(s[i]=="cookie"):
            if(s[i+1]!="milk"):
                flag+=1
                break
    if(flag==0):
        print("YES")
    else:
        print("NO")
                
