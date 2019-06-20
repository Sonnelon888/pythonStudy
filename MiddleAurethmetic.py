a, b = (int(input()) for _ in range(2))
print(((a+(3-a%3)%3)+b-(b%3))/2)