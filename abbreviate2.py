phrase, b = input()+'.', 0
prev = phrase[0]
for i in phrase:
    if prev != i:
        print(prev + str(b), end='')
        b = 0
        prev = i
    b += 1
