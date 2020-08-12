s=input()
for t in range(int(input())):
    a=input()
    x=-1
    for i in a:
        if i in s:
            continue       
        else:
            print("No")
            break
    else:
        print("Yes")
        
