for _ in range(int(input())):
    n=int(input())
    s=[int(i) for i in input().split()]
    if(n%2==0):
        print("no")
    else:
        k=1
        for i in range((n//2)+1):
            if(s[i]==s[n-i-1] and s[i]==k):
                k+=1
            else:
                print("no")
                k=-1
                break
        if(k==(n//2)+2):
            print("yes")
