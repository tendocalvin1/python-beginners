# # I am learning encapsulation because Django, backend systems, AI agents, and infrastructure tools are built 
# # on these ideas. If the foundation is weak, everything later feels like magic.


# Example 1: Bank Account

# This is the classic example because it clearly shows why direct access is dangerous.
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
        
    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        
        else:
            print("Insufficient funds")
            
    
    def get_balance(self):
        print(self.__balance)
        
        
account = BankAccount("Tendo", 2000)
account.deposit(1000)
account.withdraw(200)
account.get_balance()


# Example 2: Smart Thermostat

# Imagine a smart thermostat in a building.

class Thermostat:
    def __init__(self, temperature):
        self.__temperature = temperature
        
    def increase(self):
        self.__temperature += 1
        
    def decrease(self):
        self.__temperature -= 1
        
    def display_temperature(self):
        print(self.__temperature)
        
thermostat = Thermostat(22)
thermostat.increase()
thermostat.display_temperature()

# Example 3: User Permissions

# Very relevant to Django.

class User:
    def __init__(self):
        self.__is_admin = False
        
    def make_admin(self):
        self.__is_admin = False
        
    def show_role(self):
        print(self.__is_admin)
        
        
user = User()
user.make_admin()
user.show_role()