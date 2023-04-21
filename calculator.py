dict1 = {"+": lambda x, y: x + y,
         '-': lambda x, y: x - y,
         '*': lambda x, y: x * y}

try:
    print('введите два числа')
    x, y = float(input()), float(input())
    action = input()
    print(dict1[action](x, y))
except Exception as error:
    print(error)
