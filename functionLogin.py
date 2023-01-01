def func(name):
    return name
print(func('clement'))

# Parameters
def say_hello(name, message):
    print(f"hello {name}, and {message}")
# Position Argument
say_hello('clement', 'how are you doing?')

# Example II
# Default Parameters
def say_hello(name='sam', message=' how are you doing mr?'):
    print(f"hello {name}, and {message}")
    # Keyword Arguments
say_hello(name='clement', message='how are you doing?')

def sum_number(num1, num2):
    def another_func(n1, n2):
        return n1 + n2
    return another_func(num1, num2)

total = sum_number(10, 30)
print(total)

# docstring
def some_func(a):
    '''
        hello world how do you doing something
    '''
    print(a)
# help(some_func)

# *args **kwargs 
def super_func(name,*args, x='clement', **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total , name , x
print(super_func('king',1,2,3,4,5, num1 = 1, num2 = 2, num3 = 3, num4 =5))

# Rule: params, *args, defaults parameters, **kwargs