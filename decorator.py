from time import time


def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('*******')
        func(*args, **kwargs)
        print('*******')
    return wrap_func


@my_decorator
def hello(greeting, emoji=':)'):
    print(greeting, emoji)


# print(hello('hello'))

# Decorator


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'took {t2-t1} ms')
        return result
    return wrapper


@performance
def long_time():
    for i in range(1000):
        1 * 5


# long_time()

user1 = {
    'name': 'John',
    'valid': True,
}


def authenticated(fn):
    def wrapper(*args, **kwargs):
        for k in args:
            if k['valid']:
                result = fn(*args, **kwargs)
                return result
            return None

    return wrapper


def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]['valid']:
            return fn(*args, **kwargs)
    return wrapper


@authenticated
def message_friend(user):
    print('Message has been sent')


message_friend(user1)
