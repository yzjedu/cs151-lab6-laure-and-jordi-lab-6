# Course:  CS151, Dr.Yalew
# Due Date: 10/24/24
# Lab Assignment: 6
# Programmers: Jordi and Laure
# Problem Statement: Fixing prior ATM code so that it has proper error checking and functions.
# Data In: Whether it wants to deposit,withdraw,view, or exit.If user wants to deposit or withdraw then it must be a positive number
# Data Out: The ATM options, The total balance, Error message if deposit or withdraw amount isn't a positive number, and the end screen when you are done with the program
# Credits: The base code comes from a continuation of a prior lab

# Constants that will allow the program to run smoothly
INITIAL_BALANCE = 1000
SENTINEL = 'E'
current_balance = INITIAL_BALANCE

def display_menu(): #Setup screen for the user
    print("\nPlease select an option:"
          "\n\t D - Deposit"
          "\n\t W - Withdraw"
          "\n\t V - View Balance"
          "\n\t E - Exit")

def get_user_choice(): # Function to get the user input to see what it wants to do at the atm
    user_choice = input("Your choice: ").strip().upper()
    while user_choice not in ['D', 'W', 'V', 'E']:
        print("Error: Invalid choice. Please enter D, W, V, or E.")
        user_choice = input("Your choice: ").strip().upper()
    return user_choice

def get_positive_amount(action): #Only allows for a positive to be entered
    while True:
            amount = float(input(f"Enter the amount to {action}: ").strip())
            if amount <= 0:
                print("Error: Please enter a positive number.")
            else:
                return amount

def deposit(balance): # Allows user to deposit money into the atm
    deposit_amount = get_positive_amount("deposit")
    balance += deposit_amount
    print(f"Deposit successful! Your new balance is ${balance:.2f}.")
    return balance

def withdraw(balance): # Enables the user to withdraw from the atm
    withdraw_amount = get_positive_amount("withdraw")
    balance -= withdraw_amount
    print(f"Withdrawal successful! Your new balance is ${balance:.2f}.")
    if balance < 0:
        print(" WARNING: You have a negative balance. You will be charged 5% interest.")
    return balance

def view_balance(balance): # Views balance
    print(f"Your current balance is ${balance:.2f}.")

# Program execution starts here
print("The purpose of this program is that the user can use this as an ATM.")
user_choice = ''
while user_choice != SENTINEL:
    display_menu()
    user_choice = get_user_choice()
    if user_choice == 'D':
        current_balance = deposit(current_balance)
    elif user_choice == 'W':
        current_balance = withdraw(current_balance)
    elif user_choice == 'V':
        view_balance(current_balance)
    elif user_choice == 'E':
        print("Thank you for using the ATM program. Goodbye!")


