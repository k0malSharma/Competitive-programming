for _ in range (int(input())):
    rt=int(input())
    tr=[int(i) for i in input().split()]
    rd=int(input())
    dr=[int(i) for i in input().split()]
    st=int(input())
    ts=[int(i) for i in input().split()]
    sd=int(input())
    ds=[int(i) for i in input().split()]
    count=0
    for t in set(ts):
        if t in set(tr):
            count+=1
    for d in set(ds):
        if d in set(dr):
            count+=1
    if count==(len(set(ts))+len(set(ds))):
        print("yes")
    else:
        print("no") 
