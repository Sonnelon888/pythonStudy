phrase, b, c = input(), 0, 0
for letter in phrase:
    if letter == phrase[b]:
        c += 1
        if letter != phrase[b+2] or letter == phrase[-1]:
            print(letter + str(c), end='')
    elif letter != phrase[0] and not letter == phrase[b]:
        c = 1
        print(letter + str(c), end='')
    b += 1

