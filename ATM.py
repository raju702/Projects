from datetime import datetime

class User:
    def __init__(self, username, pin):
        self.username = username
        self.__pin = pin
        self.cur_bal = 0.00

    def validate_credentials(self):
        pin = input(f"Enter PIN for user {self.username}: ")
        if self.__pin == pin:
            print(f"Login Successful for user {self.username}")
            return pin
        else:
            print(f"Incorrect PIN for user {self.username}")
            return None

class Bank:
    def __init__(self):
        self.users = {
            "user1": User("user1", "1234"),
            "user2": User("user2", "5678")
            # Add more users as needed
        } 

    def select_user(self):
        username = input("Enter your username: ")
        return self.users.get(username)

    def get_transaction_amount(self, prompt):
        while True:
            try:
                amount = float(input(prompt))
                if amount > 0:
                    return amount
                else:
                    print("Invalid amount. Please enter a positive value.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    def deposit(self, user):
        pin = user.validate_credentials()
        if pin is not None:
            dep = self.get_transaction_amount(f"Enter amount to deposit for user {user.username}: ")
            print("Deposit in processing...")
            user.cur_bal += dep
            print("Deposit Successful")
            print(f"Your current balance is Rs.{user.cur_bal}/-")
            return dep
        return 0

    def withdraw(self, user):
        pin = user.validate_credentials()
        if pin is not None:
            withd = self.get_transaction_amount(f"Enter amount to withdraw for user {user.username}: ")
            if 0 < withd <= user.cur_bal:
                print("Withdraw in processing...")
                user.cur_bal -= withd
                print("Withdrawal Successful")
                print(f"Your current balance is Rs.{user.cur_bal}/-")
                return withd
            else:
                print("Invalid withdrawal amount or insufficient balance")
        return 0

    def statement(self, user, transaction_type, amount):
        print("----------------------------")
        print("          SBI 💐")
        print("----------------------------")
        print(f"User: {user.username}")
        print(f"Transaction Type: {transaction_type}")
        print(f"Transaction Amount: Rs.{amount}/-")
        print(f"Current Balance: Rs.{user.cur_bal}/-")
        print(f"Transaction Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Main program
bank = Bank()

selected_user = bank.select_user()

if selected_user:
    print(' 1) Balance \n----------------------------\n 2) Deposit \n----------------------------\n 3) Withdraw \n')
    n = int(input("Enter the option: "))

    if n == 1:
        print(f"Balance for user {selected_user.username}: Rs.{selected_user.cur_bal}/-")
    elif n == 2:
        deposit_amount = bank.deposit(selected_user)
        stm = input("Do you want to print a statement? (Yes/No): ")
        if stm.lower() == "yes":
            bank.statement(selected_user, "Deposit", deposit_amount)
    elif n == 3:
        withdrawal_amount = bank.withdraw(selected_user)
        stm = input("Do you want to print a statement? (Yes/No): ")
        if stm.lower() == "yes":
            bank.statement(selected_user, "Withdrawal", withdrawal_amount)
    else:
        print("Invalid option")
else:
    print("User not found.")

