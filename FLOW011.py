for _ in range(int(input())):
    s=int(input())
    if s<1500:
        gs=s+(s*0.9)+(s*0.1)
    else:
        gs=s+500+(0.98*s)
    print(gs)
