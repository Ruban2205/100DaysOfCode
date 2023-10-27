# Create a program to simulate a simple banking system with accounts.
print("\nRuban Gino Singh - Day 31 of #100DaysOfCode\n")

print("Python program to simulate a simple banking system with accounts.\n")

import os

class BankAccount:
    def __init__(self, account_number, name, balance=0.0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid withdrawal amount or insufficient funds."

    def get_balance(self):
        return f"Account balance for {self.name} (Account {self.account_number}): ${self.balance}"

    def __str__(self):
        return f"Account {self.account_number}: {self.name}"

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, name):
        if account_number not in self.accounts:
            self.accounts[account_number] = BankAccount(account_number, name)
            return f"Account {account_number} created for {name}."
        else:
            return "Account already exists."

    def get_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            return "Account not found."

    def remove_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            return f"Account {account_number} removed."
        else:
            return "Account not found."

    def list_accounts(self):
        return "\n".join([str(account) for account in self.accounts.values()])

    def save_data(self, filename):
        with open(filename, 'w') as file:
            for account in self.accounts.values():
                file.write(f"{account.account_number},{account.name},{account.balance}\n")

    def load_data(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                for line in file:
                    account_data = line.strip().split(',')
                    if len(account_data) == 3:
                        account_number, name, balance = account_data
                        self.accounts[account_number] = BankAccount(account_number, name, float(balance))
        else:
            return "Data file not found."

def main():
    bank = Bank()

    data_file = "bank_data.txt"
    bank.load_data(data_file)

    while True:
        print("\nBanking System Menu:")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. List Accounts")
        print("6. Remove Account")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            account_number = input("Enter account number: ")
            name = input("Enter account holder's name: ")
            print(bank.create_account(account_number, name))
        elif choice == '2':
            account_number = input("Enter account number: ")
            account = bank.get_account(account_number)
            if account != "Account not found.":
                amount = float(input("Enter the amount to deposit: "))
                print(account.deposit(amount))
            else:
                print(account)
        elif choice == '3':
            account_number = input("Enter account number: ")
            account = bank.get_account(account_number)
            if account != "Account not found.":
                amount = float(input("Enter the amount to withdraw: "))
                print(account.withdraw(amount))
            else:
                print(account)
        elif choice == '4':
            account_number = input("Enter account number: ")
            account = bank.get_account(account_number)
            print(account.get_balance())
        elif choice == '5':
            print(bank.list_accounts())
        elif choice == '6':
            account_number = input("Enter account number to remove: ")
            print(bank.remove_account(account_number))
        elif choice == '7':
            bank.save_data(data_file)
            print("Thank you for using the banking system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

# --------------------------------------------------------- #