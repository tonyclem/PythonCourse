from random import randint
import sys
# generate a random number 1 ~ 10
answer = randint(int(sys.argv[1]), int(sys.argv[2]))
# input from user?
# check that input is a number 1 ~ 10
while True:
    try:
        guess = int(input('guess a number 1 ~ 10: '))
        if 0 < guess < 11:
            if guess == answer:
                print('you are a genius!')
                break
        else:
            print('hey bozo, i said 1 ~ 10')
    except ValueError:
        print('enter a number from 1 to 10')
        break
# check if number is the right guess. otherwise
