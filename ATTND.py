for _ in range(int(input())):
    n=int(input())
    s=[]
    copy = []
    for i in range(n):
        s.append(input())
        copy.append(s[i].split()[0])
    copy = sorted(copy)
    repeated = []
    j = 1
    for i in copy:
        if i in copy[j:]:
            repeated.append(i)
        j+=1
    for i in range(n):
        if s[i].split()[0] in repeated:
            print(s[i])
        else:
            first = s[i].split()
            print(first[0])
