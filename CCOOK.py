for _ in range(int(input())):
    a=[int(i) for i in input().split()]
    c=0
    for i in a:
        if(i==1):
            c+=1
    if(c==0):
        print("Beginner")
    elif(c==1):
        print("Junior Developer")
    elif(c==2):
        print("Middle Developer")
    elif(c==3):
        print("Senior Developer")
    elif(c==4):
        print("Hacker")
    else:
        print("Jeff Dean")
    
    
