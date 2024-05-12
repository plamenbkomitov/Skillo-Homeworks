import math


def triangle_area(a, b, c):
    return ((4 * a * a * b * b - (a * a + b * b - c * c) ** 2) ** 0.5) / 4


def rectangle_area(a, b):
    return a * b


def square_area(a):
    return a * a


def circle_area(r):
    return math.pi * r ** 2
