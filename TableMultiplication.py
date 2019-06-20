a, b, c, d = (int(input()) for x in range(4))
i1, i2 = set(), set()
for i in range(a, b + 1):
    i1.add(i)
for j in range(c, d + 1):
    i2.add(j)
for k in sorted(i2):
    print('\t' + str(k), end='')
for l in sorted(i1):
    print('\n' + str(l), end='')
    for n in sorted(i2):
        print('\t' + str(l * n), end='')
