a, b, c, d = (int(input()) for x in range(4))
print('', *range(c,d+1), sep='\t')
for x in range(a, b+1):
    print(x, *[y*x for y in range(c, d+1)], sep='\t')