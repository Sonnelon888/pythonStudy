import statistics
a = int(input())
b = int(input())
c = int(input())
print(str(max(a, b, c)) + "\n" + str(min(a, b, c)) + "\n" + str(statistics.median([a, b, c])))