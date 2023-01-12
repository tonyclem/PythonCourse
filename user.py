class User():
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')

    def attack(self):
        print('do nothing')

    def examples(self):
        print("still testing examples")


class Wizard(User):
    def __init__(self, name, power, email):
        # User.__init__(self, email)
        super().__init__(email)  # same as above code
        self.name = name
        self.power = power

    def attack(self):
        # User.attack(self)
        # User.examples(self)
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left of {self.num_arrows}')


wizard1 = Wizard("Merlin", 50, 'merlin@gmail.com')
archer1 = Archer("Robin", 100)
# wizard1.attack()
# print(wizard1.sign_in())

# # Inheritance
# print(isinstance(wizard1, Wizard))
# print(isinstance(wizard1, object))
# print(isinstance(wizard1, User))

# polymorphism


# def player_attack(char):
#     char.attack()


# player_attack(wizard1)
# player_attack(archer1)
# print(wizard1.attack())

print(wizard1.email)
