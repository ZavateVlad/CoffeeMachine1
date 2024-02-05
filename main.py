from data import MENU


def coins():
    print('Please insert coins.')
    number_quarters = int(input('How many quarters?: '))
    number_dimes = int(input('How many dimes?: '))
    number_nickles = int(input('How many nickles?: '))
    number_pennies = int(input('How many pennies?: '))
    quarter = 0.25
    dimes = 0.10
    nickel = 0.05
    penny = 0.01
    total = (number_pennies * penny) + (number_nickles * nickel) + (number_quarters * quarter) + (number_dimes * dimes)
    return total


def asd(drink, water, coffee, milk, money):
    money = money - MENU[drink]['cost']
    if drink == 'latte' or drink == 'cappuccino':
        water -= MENU[drink]['ingredients']['water']
        coffee -= MENU[drink]['ingredients']['coffee']
        milk -= MENU[drink]['ingredients']['milk']
    elif drink == 'espresso':
        water -= MENU[drink]['ingredients']['water']
        coffee -= MENU[drink]['ingredients']['coffee']

    return drink, water, coffee, milk, money


def machine():
    is_working = True
    types_of_coffee = ['espresso', 'latte', 'cappuccino']
    water = 300
    milk = 200
    coffee = 100
    money = 0
    while is_working:
        user_input = input('What would you like? (espresso/latte/cappuccino): ')
        if user_input in types_of_coffee:
            if water < MENU[user_input]['ingredients']['water']:
                is_working = False
                print("Not enough water")
            if coffee < MENU[user_input]['ingredients']['coffee']:
                is_working = False
                print("Not enough coffee")
            if user_input == 'latte' or user_input == 'cappuccino':
                if milk < MENU[user_input]['ingredients']['milk']:
                    is_working = False
                    print("Not enough milk")

            if is_working:
                money = coins()
                drink, water, coffee, milk, money = asd(user_input, water, coffee, milk, money)
                print(f'This is your change: {money}')
        if user_input == 'report':
            print(f"Water: {water}ml \nMilk: {milk}ml \nCoffee: {coffee}g \nMoney:{money}")


machine()














