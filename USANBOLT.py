import math
for q in range(int(input())):
    bolt,tiger,a,v=[int(i) for i in input().split()]
    tiger+=bolt
    time_bolt=bolt/v
    time_tiger=math.sqrt((2*tiger)/a)
    if(time_bolt<time_tiger):
        print("Bolt")
    else:
        print("Tiger")
    
