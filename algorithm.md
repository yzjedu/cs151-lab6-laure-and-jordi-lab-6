# Algorithm Document
#### PLEASE! PLEASE! PLEASE! THINK before you code...
1. Initialize variables:
    1. INITIAL_BALANCE = 1000
    2. SENTINEL = 'E'
    3. current_balance = INITIAL_BALANCE
    4. user_choice = ''

* Purpose: Display ATM menu options to the user
* Name: display_menu
* Parameters: None
* Return: None
* Algorithm:
  1. Print the following menu options:
  'D' - Deposit
  'W' - Withdraw
  'V' - View Balance
  'E' - Exit

* Purpose: Get a valid user choice from the menu
* Name: get_user_choice
* Parameters: None
* Return: User's choice (a valid menu option)
* Algorithm:
  1. Ask the user for their choice and convert it to uppercase.
  2. While the choice is not one of 'D', 'W', 'V', 'E':
     1. Output an error message.
     2. Prompt the user to enter a valid option.
  3. Return the valid choice.

* Purpose: Get a positive amount from the user for deposit/withdrawal
* Name: get_positive_amount
* Parameters: action (string indicating "deposit" or "withdraw")
* Return: Positive amount entered by the user
* Algorithm:
  1. Ask the user to enter the amount to deposit or withdraw.
  2. While the entered amount is not a positive number:
     1. Output an error message.
     2. Prompt the user to enter a positive number.
  3. Return the positive amount. 

* Purpose: Handle the deposit operation and update balance
* Name: deposit
* Parameters: balance (current balance)
* Return: Updated balance after deposit
* Algorithm:
  1. Call get_positive_amount("deposit") to get the deposit amount.
  2. Add the deposit amount to the balance.
  3. Output a success message showing the new balance. 
  4. Return the updated balance.
 
* Purpose: Handle the withdrawal operation, apply penalties if necessary, and update balance
* Name: withdraw
* Parameters: balance (current balance)
* Return: Updated balance after withdrawal
* Algorithm:
  1. Call get_positive_amount("withdraw") to get the withdrawal amount.
  2. Subtract the withdrawal amount from the balance.
  3. Output a success message showing the new balance.
  4. If the balance is negative:
     1. Output a warning about the 5% penalty.
  5. Return the updated balance.

* Purpose: Display the current balance to the user
* Name: view_balance
* Parameters: balance (current balance)
* Return: None
* Algorithm:
  1. Print the current balance.

2. Output: "Welcome to the ATM program! This program allows you to interact with your account balance.
3. While user_choice does not equal "E":
   1. Use function display_menu
   2. Set user_choice = to function get_user_choice
   3. If user_choice == 'D':
      1. current_balance = to the function deposit(current_balance)
   4. Otherwise if user_choice == 'W':
      1. current_balance = to the function withdraw(current_balance)
   5. Otherwise if user_choice == 'V':
      1. view_balance(current_balance)
   6. Otherwise if user_choice == 'E':
      1. Output: "Thank you for using the ATM program. Goodbye!"





