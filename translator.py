from translate import Translator

translator = Translator(to_lang="japanese")

try:
    with open('test.txt', mode='r') as my_file:
        outPut = my_file.read()
        translation = translator.translate(outPut)
        with open('./test-ja.txt', mode='w') as my_file2:
            my_file2.write(translation)
        # print(translation)
except FileExistsError as err:
    print('file does not exist')
    raise err
