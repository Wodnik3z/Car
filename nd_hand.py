from new_car import New_car


class scn_car(New_car):
    def __init__(self, name, type, color, hpPower, milage):
        super().__init__(name, type, color, hpPower)
        self.milage = milage


new_1 = scn_car('Toyota', 'Supra', 'Red', 255, 2155)
new_2 = scn_car('Toyota', 'GR86', 'Red', 228, 2138)

def nd_hand():
    new_1 = scn_car('Toyota', 'Supra', 'Red', 255, 2155)
    new_2 = scn_car('Toyota', 'GR86', 'Red', 228, 2138)

    print(new_2.milage)