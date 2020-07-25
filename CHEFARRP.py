for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i  in input().split()]
    count = 0
    for i in range(n):
        for j in range(i+1, n+1):
            sub = a[i:j]
            s = sum(sub)
            p = 1
            for k in sub:
                p*= k
            if s == p:
                count += 1
    
    print(count)
