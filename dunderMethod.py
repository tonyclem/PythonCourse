class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            "name": 'Yoyo',
            "has_pets": False,
        }

    def __str__(self):
        return f'{self.color}'

    def __len__(self):
        return 5

    def __del__(self):
        print('delete')

    def __call__(self):
        print("call yes!")

    def __getitem__(self, i):
        return self.my_dict[i]


action_figure = Toy('red', 0)
print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
# del action_figure
print(action_figure())
print(action_figure['name'])

# exercise get 1000


class SuperList(list):
    def __len__(self):
        return 1000


super_list = SuperList()

print(len(super_list))
super_list.append(5)
print(super_list[0])
print(issubclass(list, object))
