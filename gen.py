def prime_generator(n):
    mas = [1 for i in range(n)]
    mas[0], mas[1] = 0, 0
    for i in range(n):               # цикл по индексам до н
        if mas[i]:
            yield i
            for m in range(i * 2, n, i):
                mas[m] = 0
for prime in prime_generator(21):              # итер до нашего
    print(prime)
class CycleIterator:
    def __init__(self, iterable):              # прин сп кот цикл повт
        self.iterable = iterable               # сохр передан об
        self.index = 0
        self.length = len(iterable)            # сохр
    def __iter__(self):                        # возв об чтобы ц перебрал
        return self
    def __next__(self):                        # опр мет для получ сл эл
        current = self.iterable[self.index]            # получ эл по инд
        self.index = (self.index + 1) % (self.length)         # обн инд
        return current
it = CycleIterator([1, 2, 3])             # созд экз
for _ in range(10):
    print(next(it))