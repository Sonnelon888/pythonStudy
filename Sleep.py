x = int(input())
h = int(input())
m = int(input())
if (x % 60) + m >= 60:
    n = (x % 60 + m) //60
    print (x // 60 + n + h)
    print ((x % 60 + m ) % 60)
else:
    print(x // 60 + h)
    print(x % 60 + m)