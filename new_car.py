# def new():

class New_car:
    change_c = 'Black'
    num_of_cars = 3

    # change_c = str(input("Change the basic color"))

    def __init__(self, name, type, color, hpPower):
        self.name = name
        self.type = type
        self.color = color
        self.hpPower = hpPower

        New_car.num_of_cars -= 1

    def fullspec(self):
        return '{} {} {} {}'.format(self.name, self.type, self.color, self.hpPower)

    def change_color(self):
        self.color = New_car.change_c

    # @classmethod
    # def change_names(cls, change_n):
    # cls.name = change_n


class scn_car(New_car):
    def __init__(self, name, type, color, hpPower, milage):
        super().__init__(name, type, color, hpPower)
        self.milage = milage


new_1 = scn_car('Toyota', 'Supra', 'Red', 255, 2155)
new_2 = scn_car('Toyota', 'GR86', 'Red', 228, 2138)

# print(new_1.name)
print(new_2.fullspec())
new_2.change_color()
print(new_2.fullspec())
print('num of cars left ', New_car.num_of_cars)
print('Milage: ', new_2.milage, 'of car', new_2.name, new_2.type)

def new():
    new_1 = scn_car('Toyota', 'Supra', 'Red', 255, 2155)
    new_2 = scn_car('Toyota', 'GR86', 'Red', 228, 2138)

    # print(new_1.name)
    print(new_2.fullspec())
    new_2.change_color()
    print(new_2.fullspec())
    print('num of cars left ', New_car.num_of_cars)
    print('Milage: ', new_2.milage, 'of car', new_2.name, new_2.type)