import math

def square(x):
    return x**2

def areaofcircle(radius):
    area = math.pi * square(radius)
    return area

print(areaofcircle(5))