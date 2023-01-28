my_file = open('test.txt')

print(my_file.readlines())
# my_file.seek(0)


try:
    with open('test.txt', mode='r+') as my_file:
        text = my_file.write('hello mr don')
        print(text)
except FileExistsError as err:
    print('file does not exist')
    raise err
except IOError as err:
    print("IO error")
    raise err
