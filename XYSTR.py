for _ in range(int(input())):
    s=input()
    i=0
    p=0
    while(i<((len(s)-1))):
        if(s[i]!=s[i+1]):
            i+=1
            p+=1
        else:
            pass
        i+=1
    print(p)
