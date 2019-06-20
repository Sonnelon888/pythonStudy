a, b, c = [int(i) for i in input().split()], 0, 0
for i in a:
    if len(a) == 1:
        print(i)
    elif c == 0:
        print(a[-1] + a[1])
    elif c == len(a)-1:
        print(int(a[0]) + int(a[c-1]))
    elif c in range(1, len(a)-1):
        print(int(a[c+1]) + int(a[c-1]))

    c += 1