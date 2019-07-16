for _ in range(int(input())):
    a=int(input())
    c=0
    s=input()
    for i in s:
        if(i=='I'):
            c=1
            break
        elif(i=='Y'):
            c=2
        else:
            if(c==2 or c==1):
                c=2
            else:
                c=3
    if(c==1):
        print("INDIAN")
    if(c==2):
        print("NOT INDIAN")
    if(c==3):
        print("NOT SURE")
    
