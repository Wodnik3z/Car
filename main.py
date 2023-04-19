from new_car import new
from nd_hand import nd_hand
from leasing import leasing

def menu():
    print('Welcome to car dealership, how can I help you?')
    print('[1] Buy a new car')
    print('[2] Buy a 2nd hand car')
    print('[3] Leasing')
    print('[0] Exit')


def option3():
    print("yo")


menu()
option = int(input("Choose Option from [0-3]: "))

while option != 0:
    if option == 1:
        # do 1
        new()
    elif option == 2:
        # do 2
        nd_hand()
    elif option == 3:
        # do 3
        leasing()
    else:
        print("invalid option.")

    print('')
    menu()
    option = int(input("Choose Option from [0-2]: "))

print("bayo")
