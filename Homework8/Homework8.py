import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_type(self):
        return self.__class__

    def get_sides(self):
        r = self.radius
        return f'{r=}'

    def get_perimeter(self):
        return 2 * math.pi * self.radius

    def get_area(self):
        return math.pi * self.radius ** 2


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_type(self):
        return self.__class__

    def get_sides(self):
        return f'a={self.a} b={self.b}'

    def get_perimeter(self):
        return (self.a + self.b) * 2

    def get_area(self):
        return self.a * self.b


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_type(self):
        return self.__class__

    def get_sides(self):
        return f'a={self.a} b={self.b} c={self.c}'

    def get_perimeter(self):
        return self.a + self.b + self.c

    def get_area(self):
        half_perim = (self.a+self.b+self.c)/2
        return math.sqrt(half_perim*(half_perim-self.a)*(half_perim-self.b)*(half_perim-self.c))


def get_class(raw_input):
    values = [int(x) for x in raw_input.split()]
    if len(values) == 1:
        r = int(raw_input)
        if r <= 0:
            print('There can\'t be a circle with 0 or smaller radius')
            return
        return Circle(r)
    if len(values) == 2:
        a, b = values
        if a <= 0 or b <= 0:
            print('There can\'t be a square or a rectangle with 0 or smaller side')
            return
        return Rectangle(a, b)
    if len(values) == 3:
        a, b, c = values
        if a <= 0 or b <= 0 or c <= 0:
            print('There can\'t be a triangle with 0 or smaller side')
            return
        elif a + b <= c or a + c <= b or b + c <= a:
            print('There can\'t be a triangle where sum of 2 sides is less or equal to the 3-rd one')
            return
        return Triangle(a, b, c)


if __name__ == '__main__':
    inform = input()
    object = get_class(inform)
if object is not None:
    print(object.get_type())
    print(object.get_sides())
    print(object.get_perimeter())
    print(object.get_area())