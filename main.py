"""
Credits: Gabriel Onyedika Nnamoko 24/06/2022 4.31pm

This is a basic betting app. I have not modified the logic of generating odds to my taste. I will work on that!
"""

import random

def odd_generator(user_balance):
    step = random.randint(10, 23000)
    balance_on_which_to_reduce_odd = random.randrange(1000, 100000000, step)
    numbers = random.randrange(1, 4)
    first_start = random.randint(1,3)
    first_stop = random.randint(4, 5)
    second_start = random.randint(1, 5)
    second_stop = random.randint(6, 250)
    if (numbers//2) != numbers/2:
        if user_balance == balance_on_which_to_reduce_odd:
            odd = random.randrange(1, 4)
        else:
            odd = random.randrange(first_start, first_stop)
    else:
        if user_balance == balance_on_which_to_reduce_odd:
            odd = random.randrange(1, 4)
        else:
            odd = random.randrange(second_start, second_stop)
    return odd

def deposit_money():
    deposited_amount = int(input("Enter amount you want to deposit: "))
    return deposited_amount

def deposit_again():
    new_deposit = deposit_money()
    return new_deposit

def betting_categories():
    categories = [10, 20, 50, 100, 150, 200, 250, 300, 350, 400, 500, 1000, 2000, 5000, 10000]
    return categories

def bet_controller():
    amount_user_deposited = deposit_again()
    bet_categories = betting_categories()
    company_balance = 0
    user_current_balance = 0
    while amount_user_deposited != 0:
        condition = True
        print("\nBetting Prices (Select an amount to bet):")
        counter = 1
        odd_counter = 1
        for amounts in bet_categories:
            print(f"{counter}. ${amounts:,}", end='\n')
            counter += 1
        print("\nOr enter a custom value to bet")
        user_input = int(input("\nSelect a number (or enter a custom value to place bet): "))
        try:
            user_amount = bet_categories[user_input-1]
        except:
            user_amount = user_input
        while condition:
            if user_amount > amount_user_deposited:
                checker = 0
                for numbers in bet_categories:
                    if user_amount > numbers:
                        checker += 1
                    else:
                        continue
                if checker >= 1:
                    user_input = int(input("\n\tEnter a lower amount: "))
                    user_amount = bet_categories[user_input - 1]
                else:
                    print("\nYour balance is too low! Deposit!")
                    deposit_again()
            else:
                staked_amount = user_amount
                user_current_balance = amount_user_deposited - staked_amount
                condition = False

        odd = odd_generator(user_current_balance)
        user_prediction = int(input("\nAt what odd do you want to cash out?\n\t"))
        while odd_counter <= odd:
            current_odd = odd_printer(odd_counter)
            if odd_counter == user_prediction:
                print("\nCurrent odd matches your prediction!\n")
                user_balance = staked_amount * odd_counter
                user_current_balance = amount_user_deposited + user_balance
                print(f"\nCongratulations! ${user_balance:,} has been added to your account!\n\nYour new balance is ${user_current_balance:,}")
                print(f"\nThe winning odd was {odd}X")
                break
            elif odd_counter == odd and odd_counter != user_prediction:
                print(f"\nSorry, you lost ${staked_amount:,}. The winning odd was {odd}X. Better luck next time!")
                company_balance += staked_amount
                print(f"\nThe company has ${company_balance:,}")
                break
            else:
                odd_counter += 1

        amount_user_deposited = user_current_balance

    if amount_user_deposited == 0:
        user_choice = int(input(f"\nYou cannot place new bets as your account balance is ${amount_user_deposited} currently\n\nDo you want"
                                f" to fund your wallet now?\n\t1. Yes\n\t2. No\n\n"))

        if user_choice == 1:
            bet_controller()
        else:
            print("\nSession Ended.")

def odd_printer(odd_counter):
    import datetime as dt
    output = print(f"Current Odd: {odd_counter}X\n")
    current_time = dt.datetime.now()
    time_interval = dt.timedelta(seconds=1)
    time_to_next_odd_printing = current_time + time_interval
    while current_time <= time_to_next_odd_printing:
        if current_time == time_to_next_odd_printing:
            return output
        else:
            current_time = dt.datetime.now()


bet_controller()