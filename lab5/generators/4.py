def squeres(x, y):
    while(x <= y):
        yield x ** 2
        x += 1

a = int(input())
b = int(input())

for i in squeres(a, b):
    print(i)