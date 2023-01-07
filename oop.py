# OOP

class Dog:

    # class attribute
    # attr1 = "mammal"

    # Instance attribute
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("My name is {}".format(self.name))


# Driver code
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

# Accessing class methods
Rodger.speak()
Tommy.speak()

# Example II


class PlayerCharacter:
    # Class Object Attribute
    membership = True

    # Instance attributes
    def __init__(self, name, age):
        if self.membership:
            self.name = name  # attributes
            self.age = age

    def run(self):
        # print(f"My name is {self.name}")
        print('run')


player1 = PlayerCharacter('clement', 20)
player2 = PlayerCharacter('king', 100)
player2.attack = 20
# PlayerCharacter(player1.run())
player1.run()
player2.run()
print(player1.name)
print(player2.attack)


# Example III
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        x = 3
        if age >= 4:
            self.name = name
            self.age = age

    def oldest_func(self):
        print(f"Then oldest cat is {self.age} old")
        return


cat1 = Cat('love', 3)
cat2 = Cat('nice', 2)
cat1 = Cat('great', 4)
cat1.oldest_func()


# Example
class PlayerCharacter:
    # Class Object Attribute
    membership = True

    # Instance attributes
    def __init__(self, name, age):
        if self.membership:
            self.name = name  # attributes
            self.age = age

    def run(self):
        # print(f"My name is {self.name}")
        print('run')

    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2


player1 = PlayerCharacter('clement', 20)
print(player1.adding_things(5, 5))
