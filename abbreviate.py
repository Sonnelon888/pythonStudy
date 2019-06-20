phrase, b, prev = input()+'.', 0, 0
for i in phrase:
    if prev == i:
        b += 1
    elif prev == 0:
        prev = i
        b += 1
    elif prev != i:
        print(str(prev) + str(b), end='')
        prev = i
        b = 1
