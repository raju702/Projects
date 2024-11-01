# ATM Simple Banking System

This is a Python-based banking system that allows users to authenticate, check balance, deposit, withdraw, and print transaction statements. The program demonstrates object-oriented programming principles in Python.

Features
User Authentication: Each user has a unique PIN for secure access to their account.
Balance Inquiry: Users can check their current balance.
Deposit and Withdrawal: Users can deposit funds and withdraw funds (if balance allows).
Transaction Statements: Option to print transaction statements that include the type of transaction, amount, and time.
Project Structure
User Class: Represents a bank user with attributes such as username, pin, and cur_bal (current balance).

validate_credentials(): Verifies the user's PIN before performing any transaction.
Bank Class: Represents the bank system, handling user selection and transactions.

select_user(): Prompts the user to enter their username and retrieves the user object if it exists.
get_transaction_amount(prompt): Ensures the transaction amount is valid and positive.
deposit(user): Validates the user and processes the deposit transaction.
withdraw(user): Validates the user, checks balance, and processes the withdrawal.
statement(user, transaction_type, amount): Prints a formatted statement of the transaction.
Usage
Run the program.
Login by entering your username.
Choose a transaction:
1 for balance inquiry.
2 for deposit.
3 for withdrawal.
For deposit/withdrawal, follow the prompts to complete the transaction and choose if you’d like a statement printed.
Enter your username: user1
1) Balance 
2) Deposit 
3) Withdraw 

Enter the option: 2
Enter PIN for user user1: ****
Enter amount to deposit for user user1: 5000
Deposit Successful
Your current balance is Rs.5000.0/-
Do you want to print a statement? (Yes/No): Yes

Requirements
Python 3.x
Future Enhancements
User Registration: Allow users to self-register.
Multi-user Support: Enable the system to handle more complex user data storage.
Transaction History: Keep a record of all transactions.
License
This project is open-source and available under the MIT License.
