while True:
    try:
        age = int(input('what is your age? '))
    except ValueError:
        print('Please enter a number')
    except ZeroDivisionError:
        print('Please enter age higher than zero')
    else:
        print('thank you')
        break
    finally:
        print('ok, i am finally done')


def sum_num(num1, num2):
    try:
        return num1 + num2
    except (TypeError, ZeroDivisionError) as err:
        print(err)
