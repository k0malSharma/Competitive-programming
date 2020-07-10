for _ in range(int(input())):
    x,y,z=[int(i) for i in input().split()]
    if x+y-z==0 or x+z-y==0 or z+y-x==0:
            print('yes')
    else:
            print('no')
