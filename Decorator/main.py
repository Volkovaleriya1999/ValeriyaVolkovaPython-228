class Power:
    def __init__(self, func):
        self.func = func

    def __call__(self, a, b, c):
        rv = self.func(a, b) ** c
        return 'Результат работы декоратора: ', rv

@Power
def func(a, b):
    return a * b

print(func(2, 2, 3))