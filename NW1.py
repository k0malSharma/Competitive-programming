for _ in range(int(input())):
    n,st1=input().split()
    n=int(n)
    s=[0]*7
    st=["mon", "tues", "wed", "thurs", "fri", "sat" , "sun"]
    b=st.index(st1)
    for i in range(n):
        s[b]+=1
        if(b!=6):
            b+=1
        else:
            b=0
    print(*s)
    
