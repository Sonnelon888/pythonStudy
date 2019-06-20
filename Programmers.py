x = int(input())
a = list(range(1, 1000, 10))
del1 = []
for i in range(2, 1000, 10):
    del1.append(i)
for i in range(3, 1000, 10):
    del1.append(i)
for i in range(4, 1000, 10):
    del1.append(i)
for i in del1:
    if i == 12 or str(i)[1:] == "12":
        del1.remove(i)
for i in del1:
    if i == 13 or str(i)[1:] == "13":
        del1.remove(i)
for i in del1:
    if i == 14 or str(i)[1:] == "14":
        del1.remove(i)
if x in a and (x != 11 and str(x)[1:] != "11"):
    print(str(x), "программист")
elif x in del1:
    print(str(x), "программиста")
# Для чисел "Программиста"
else:
    print(str(x), "программистов")
