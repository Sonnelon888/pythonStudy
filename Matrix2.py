a = input()
b = []
while a != 'end':
    b += [[int(i) for i in a.split()]]
    a = input()
for i in range(len(b)):
        for j in range(len(b[0])):
            print(b[(i-1)%len(b)][j] + b[(i+1)%len(b)][j] + b[i][(j-1)%len(b[0])] + b[i][(j+1)%len(b[0])], end=' ')
        print()