from random import randint


def run_guess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print('you are a genius!')
            return True
    else:
        print('hey bozo, i said 1 ~ 10')
        return False


# generate a random number 1 ~ 10
if __name__ == '__main__':
    answer = randint(int(1), int(20))
    # input from user?
    # check that input is a number 1 ~ 10
    while True:
        try:
            guess = int(input('guess a number 1 ~ 10: '))
            run_guess(guess, answer)
        except ValueError:
            print('enter a number from 1 to 10')
            break
    # check if number is the right guess. otherwise
