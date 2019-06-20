a = [int(i) for i in input().split()]
b = set(a)
for i in b:
    if a.count(i) > 1:
        print(int(i))
