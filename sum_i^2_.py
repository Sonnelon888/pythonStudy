a, c, d = '0', [], 0
while a != 0:
    b = int(input())
    c.append(b)
    a = int(a)
    a += b
for i in c:
    d += i * i
print(d)