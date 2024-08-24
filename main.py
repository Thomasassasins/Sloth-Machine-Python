import random
import time
from colorama import Fore

        

def spin_row():
    symbols = ["🍒" , "🍌" , "🍋" , "🧀"]

    results = []
    return [random.choice(symbols) for _ in range(3)]


def paid(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 2
        elif row[0] == "🍌":
            return bet * 3
        elif row[0] == "🍋":
            return bet * 4
        elif row[0] == "🧀":
            return bet * 5
    return 0

def space_row(row):
    print("")
    print("----------------------")
    print(" ".join(row))
    print("----------------------")
    print("")
def main():
    balance = 100

    print("----------------------")
    print("Welcome to slot machine")
    print("----------------------")

    while True:
        print(f"Your actual current is {balance}")
        bet = input("How much money do you want to bet? ")

        bet = int(bet)

        if bet <= 0:
            print("")
            print("Your bet must be greater than 0")
            continue

        if bet > balance:
            print("")
            print("You cant put more money than you currently have! ")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning ...")
        time.sleep(1)
        space_row(row)

        money = paid(row, bet)

        if money > 0:
            print(Fore.RED + f"You won! ${balance}" + "\033[39m")
        else:
            print(f"Goverment wants you to stop gambling dont give up! Your Balance is {balance}")

        balance += money

        if balance == 0:
            print(Fore.RED + "You lost :(" + "\033[39m")
            break

if main() == "__main__":
    main()
