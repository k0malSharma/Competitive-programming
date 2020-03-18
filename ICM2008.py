for _ in range(int(input())):
    a, b, c, d = (int(i) for i in input().split())
    m = abs(a-b)
    n = abs(c-d)
    if m==n or n!=0 and m%n==0:
        print('YES')
    else:
        print('NO')
