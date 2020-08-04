for _ in range(int(input())):
    x=input()
    y=input()
    p=-1
    for i in range(len(x)):
        if((x[i]!=y[i]) and (x[i]!='?' and y[i]!='?')):
           p=0
           break
    if(p==-1):
        print("Yes")
    else:
        print("No")
