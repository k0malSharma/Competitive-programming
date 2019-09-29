n=int(input())
a=[int(i) for i in input().split()]
x,y=0,0
for i in a:
    if(i%2==0):
        x+=1
    else:
        y+=1
if (x>y):
    print("READY FOR BATTLE")
else:
    print("NOT READY")
