year_conducted = [2010, 2015, 2016, 2017, 2019]
for _ in range(int(input())):
    n = int(input())
    if n in year_conducted:
        print("HOSTED")
    else:
        print("NOT HOSTED")
