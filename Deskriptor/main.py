class Verify_Side:
    @staticmethod
    def verify_side(side):
        if side <= 0:
            raise ValueError(f'Значение {side} должно быть положительным!')

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
        # return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_side(value)
        instance.__dict__[self.name] = value
        # setattr(instance, self.name, value)

class Triangle:
    a = Verify_Side()
    b = Verify_Side()
    c = Verify_Side()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def verify_triangle(self):
        if (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a):
            print(f'Треугольник со сторонами {self.a}, {self.b}, {self.c} существует.')
        else:
            print(f'Треугольник со сторонами {self.a}, {self.b}, {self.c} не существует.')

tg1 = Triangle(2, 5, 6)
tg2 = Triangle(5, 2, 8)
tg3 = Triangle(7, 3, 6)

tg1.verify_triangle()
tg2.verify_triangle()
tg3.verify_triangle()

