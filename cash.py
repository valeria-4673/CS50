from cs50 import get_float
def calculate_quarters(change):
    quarters = change // .25
    return quarters

def calculate_dimes(change):
    dimes = change // .10
    return dimes

def calculate_nickels(change):
    nickels = change // .05
    return nickels

def calculate_pennies(change):
    pennies = change // .01
    return pennies

def main():

    while True:
        change = get_float("Change: ")
        if (change >= 0):
            break

    quarters = calculate_quarters(change)
    change = change - quarters * 0.25

    dimes = calculate_dimes(change)
    change = change - dimes * 0.10

    nickels = calculate_nickels(change)
    changes = change - nickels * 0.05

    pennies = calculate_pennies(change)
    changes = change - pennies * 0.01

    coins = quarters + dimes + nickels + pennies

    print(int(coins))

main()
