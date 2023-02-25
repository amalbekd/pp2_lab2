import math

n = int(input("Input number of sides: "))
l = int(input("Input the length of a side: "))

ctg = 1 / math.tan(math.radians(180 / n))


print("The area of the polygon is:", (l ** 2) * n * ctg / 4)