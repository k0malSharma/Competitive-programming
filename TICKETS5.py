for _ in range(int(input())):
    s = input()
    n = len(s)
    flag = 0
    if (n%2!=0):
        flag=1
    elif (s[0]==s[1]) and n==2:
        flag=1
    for i in range(n):
        if i+2 < n and s[i]==s[i+2] and s[i]!=s[i+1]:
            flag=0
        else:
            break
        
    if flag==0 and i==n-2:
        print("YES")
    else:
        print("NO")
