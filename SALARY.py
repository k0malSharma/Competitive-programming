for _ in range(int(input())):
    n = int(input())
    w = [int(i) for i in input().split()]
    print(sum(w)-n*min(w))
