

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"The amount deposited is {amount}")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"The amount withdrawn is {amount}")

    def display_balance(self):
        print(f"Current balance: {self.balance}")