def make_list(num):
    result = []
    for i in range(num):
        result.append(i*2)
    return result
# print(make_list(100))


def generator_function(num):
    for i in range(num):
        yield i


for item in generator_function(100):
    # print(item)
    pass


class MyGen():
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration


gen = MyGen(0, 20)
for i in gen:
    # print(i)
    pass


def fib(number):
    if number <= 1:
        return number
    else:
        return fib(number - 1) + fib(number - 2)


for item in range(10):
    print(fib(item))
