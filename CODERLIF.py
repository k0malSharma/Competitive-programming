for _ in range(int(input())):
    a=[int(i) for i in input().split()]
    c=0
    for i in a:
        if(i==1):
            c+=1
        else:
            c=0
        if(c==6):
            c=-1
            break
    if(c!=-1):
        print("#allcodersarefun")
    else:
        print("#coderlifematters")
                    
