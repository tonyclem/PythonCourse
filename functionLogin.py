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

def sum(num1, num2):
    def another_func(n1, n2):
        return n1 + n2
    return another_func(num1, num2)

total = sum(10, 30)
print(total)