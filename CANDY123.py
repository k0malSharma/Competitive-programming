for _ in range(int(input())):
    a,b=[int(i) for i in input().split()]
    x,y,i=0,0,1
    while(True):
        if(i%2==0):
            y+=i
            if(y>b):
                print("Limak")
                break
        else:
            x+=i
            if(x>a):
                print("Bob")
                break
        i+=1
    
         
    
