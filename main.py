MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0

#TODO1 Prompt user by asking “What would you like? (espresso/latte/cappuccino):


def coin_calc():
    """"ask the user how many coins they have"""
    quaters = float(input("how many quaters? "))
    cal_quater = quaters * 0.25
    dime = float(input("how many dime? "))
    cal_dime = dime * 0.10
    nickles = float(input("how many nickles? "))
    cal_nickles = nickles * 0.05
    pennies = float(input("how many pennies? "))
    cal_pennies = pennies * 0.01

    return cal_quater + cal_dime + cal_nickles + cal_pennies

#TODO3 Print report.
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
       if order_ingredients[item] >= resources[item]:
           print(f"sorry there is not enough {item}")
           return False
    return True


def is_transaction_successful(money_received, drink_cost):
    """"return true is money is sufficient or false is not"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"here is {change} change")
        global  profit
        profit += drink_cost
        return True
    else:
        print("sorry not enough money money refunded")
        return  False

def make_coffe(drink_name, order_ingredients):
    """deduct the required ingredient from resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"here is your {drink_name} coffee ☕")




is_on = True
while is_on:
    customer_choice = input("what would you like? (espresso/latte/cappuccino) ").lower()

    if customer_choice == "off":
        is_on = False
    elif customer_choice == "report":
        print(f" water: {water}ml \n milk: {milk}ml \n coffee: {coffee}g \n money: {profit}$ ")
    else:
        drink = MENU[customer_choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = coin_calc()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffe(customer_choice, drink["ingredients"])







#TODO2 Turn off the Coffee Machine by entering “off” to the prompt.







#TODO4 Check resources sufficient?




#TODO5 Process coins.


#TODO6Check transaction successful?