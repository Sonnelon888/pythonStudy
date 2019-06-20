a = input()
b = input()
c = input()
operation = {'pow': '**', 'div': '//', 'mod': '%'}
try:
    print(eval("(" + a + ")" + operation.get(c, c) + "(" + b + ")"))
except ZeroDivisionError:
    print('Деление на 0!')
