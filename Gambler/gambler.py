#!/usr/bin/env python3.11

import random

MAX_LINES = 5
MAX_BET = 10000
MIN_BET = 1

ROWS = 5
COLS = 3

# frequency of each symbol
symbol_count = {"$": 1, "!": 2, "S": 3, "A": 4, "B": 5, "C": 6, "D": 7}

# Value of each symbol
symbol_value = {"$": 10, "!": 8, "S": 7, "A": 6, "B": 5, "C": 4, "D": 3}


# Checking for winner
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check: 
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


# Create the spin
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


# Print values
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


# depositing funds
def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("please enter a number.")

    return amount


# Getting lines
def get_number_of_lines():
    while True:
        Lines = input("Enter the number of lines to bet on (1-" +
                      str(MAX_LINES) + ")? ")
        if Lines.isdigit():
            Lines = int(Lines)
            if 1 <= Lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("please enter a number.")

    return Lines


# getting bet
def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("please enter a number.")

    return amount


# Bet and balance, printing winnings and winning lines
def spin(balance):
    Lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * Lines

        if total_bet > balance:
            print(f"Insufficient funds, your current balance is ${balance}")
        else:
            break

    print(
        f"you are betting ${bet} on {Lines} lines. Total is equal to: ${total_bet}"
    )

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, Lines, bet, symbol_value)
    print(f"You won ${winnings}! ")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet


# Main function
def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input('Press enter to play (q to quit).')
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")


main()
