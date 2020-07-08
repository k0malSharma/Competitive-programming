for _ in range(int(input())):
    b = int(input())
    if b<4:
        print(0)
        continue
    else:
        if b%2==1:
            b-=1
        print(((b-2)*(b))//8)
