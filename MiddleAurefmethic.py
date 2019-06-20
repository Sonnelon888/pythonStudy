a, b = (int(input()) for x in range(2))
s, r = 0, 0
for i in range(a, b + 1):
        if i % 3 == 0:
            r += 1
            s += i
print(s / r)