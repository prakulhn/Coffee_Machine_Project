menu = {
    'latte': {
        'ingredients': {
            'water': 200,
            'milk': 150,
            'coffee': 24
        },
        'cost': 150
    },
    'espresso': {
        'ingredients': {
            'water': 50,
            'coffee': 18
        },
        'cost': 100
    },
    'cappuccino': {
        'ingredients': {
            'water': 250,
            'milk': 100,
            'coffee': 24
        },
        'cost': 200
    },
}

profit = 0
resources = {
    'water': 1000,
    'milk': 2500,
    'coffee': 500
}


def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f'Sorry, enough resources are not available for {item}.')
            return False
    return True


def process_coins():
    print("Please insert coins.")
    total_money = 0
    coins_five = int(input('How many Rs.5 coins? '))
    coins_ten = int(input('How many Rs.10 coins? '))
    coins_twenty = int(input('How many Rs.20 coins? '))
    total_money = (coins_five*5) + (coins_ten*10) + (coins_twenty*20)
    return total_money


def is_payment_successful(money_received, coffee_cost):
    if money_received >= coffee_cost:
        global profit
        profit += coffee_cost
        change = money_received - coffee_cost
        print(f"Here's your {change} as change.")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def make_coffee(coffee_name, coffee_ingredients):
    for item in coffee_ingredients:
        resources[item] -= coffee_ingredients[item]
    print(f"Here's is your {coffee_name} ☕... Enjoy!!")


is_on = True
while is_on:
    user_choice = input('What would you like to have (latte/espresso/cappuccino)?: ')
    if user_choice == 'off':
        is_on = False
    elif user_choice == 'report':
        print(f'Water: {resources["water"]}ml \nMilk: {resources["milk"]}ml \nCoffee: {resources["coffee"]}g')
        print(f'Money: Rs.{profit}')
    else:
        coffee_type = menu[user_choice]
        print(coffee_type)
        if check_resources(coffee_type['ingredients']):
            payment = process_coins()
            if is_payment_successful(payment, coffee_type['cost']):
                make_coffee(user_choice, coffee_type['ingredients'])



