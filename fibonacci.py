def fib(number):
    if number <= 1:
        return number
    else:
        return fib(number - 1) + fib(number - 2)


for item in range(10):
    # print(fib(item))
    pass


def fib2(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        temp = a
        print('temp', temp)
        a = b
        b = temp + b


for x in fib2(10):
    print(x)
