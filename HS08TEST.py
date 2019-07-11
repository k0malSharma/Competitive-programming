a,b=input().split()
a=int(a)
b=float(b)
if((a+0.5)>b or a%5!=0):
    print("%.2f"%b)
else:
    print("%.2f"%(b-a-0.5))
