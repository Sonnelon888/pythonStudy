figure = input()
if figure == "треугольник":
    a, b, c, = int(input()), int(input()), int(input())
    print((((a + b + c) * 0.5) * (((a + b + c) * 0.5) - a) * (((a + b + c) * 0.5) - b) * (((a + b + c) * 0.5) - c))
          ** 0.5)
elif figure == "прямоугольник":
    print(int(input()) * int(input()))
elif figure == "круг":
    print(3.14 * int(input()) ** 2)
