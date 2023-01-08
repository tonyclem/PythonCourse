class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print("Starting")

    def speak(self):
        print(f"my name is {self.name}, my age is {self.age} years old")


player1 = PlayerCharacter('clement', 100)
print(player1.speak())  # is Called Abstractions


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
