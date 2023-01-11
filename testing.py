class PlayerCharacter:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def run(self):
        print("Starting")

    def speak(self):
        print(f"my name is {self._name}, my age is {self._age} years old")


player1 = PlayerCharacter('clement', 100)
player1.name = '!!!'
print(player1.speak)  # is Called Abstractions
print(player1.name)


class PlayerCharacterName():
    def __init__(self, name, age):
        self.name = name
        self.age = age


player2 = PlayerCharacterName('clement', 200)
print(player2.name)  # is Called Encapsulation
print(player2.age)

player3 = {'name': 'sunday', 'age': 200}
print(player3['name'])
print(player3['age'])


class Cat:

    def __init__(self):
        self.sound = "meow"

    def speak(self):
        print("Cat says: {}".format(self.sound))


c = Cat()
c.speak()

# change the price
c.sound = "bow-wow"
c.speak()
