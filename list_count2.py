s = input().split()
print(*(i for i in set(s) if s.count(i) > 1))
