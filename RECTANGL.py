for i in range(int(input())):
    a,b,c,d=[int(i) for i in input().split()]
    if(a==b and c==d):
        print("YES")
    elif(a==c and b==d):
        print("YES")
    elif(a==d and b==c):
        print("YES")
    else:
        print("NO")
       
