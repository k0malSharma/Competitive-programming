for _ in range(int(input())):
    n,s=input().split()
    n=int(n)
    a = [int(i) for i in input().split()]
    if n==1 and s=='Dee' and a[0]%2==0:
        print("Dee")
    else:
        print("Dum")

