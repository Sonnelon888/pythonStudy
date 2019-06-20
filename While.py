x = 0
while x is not None:
    x = int(input())
    if 10 <= x <= 100:
        print(x)
    elif x > 100:
        break