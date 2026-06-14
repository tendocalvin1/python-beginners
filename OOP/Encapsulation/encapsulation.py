# The pillars of OOP that must be covered include: Inheritance, Polymorphism, abstraction and encapsulation
# Each pillar is meant to perform a particular task given

# Simple Definition

# Encapsulation means:

# Bundling data and behavior together while controlling access to the data.

# In simpler language:

# Protect the object's important information and force people to interact with it through approved methods.

# Real World Analogy

# Think about an ATM.

# You can:

# Deposit money
# Withdraw money
# Check balance

# But can you open the ATM and directly edit:

# balance = 1,000,000

# No.

# The internal money is protected.

# You interact through approved actions.

# That's encapsulation.


# The Biggest Misconception

# Many people think:

# Encapsulation = private variables

# Wrong.

# Private variables are only one technique.

# The real idea is:

# Control how data is accessed and modified.



# Real world example for encapsulation
# first encapsulation example

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
        
    def deposit(self, amount):
        self.__balance += amount
        
    def withdraw(self, amount):
        self.__balance -= amount
    
    
    def get_balance(self):
        return self.__balance
    
# usage
account = BankAccount("Tendo", 2000)
account.deposit(1500)
account.withdraw(500)

print(account.get_balance())

# print(account.__balance) # This generates an Error because the balance is Protected.

# Exercises on encapsulation
# Questions to answer: How do we protect the object's data?
# Answer to the question: Only allow approved interactions

# Number one
class User:
    def __init__(self, password):
        self.__password = password
        
    def change_password(self, password):
        self.__password = password
        
    def show_password(self):
        print(user.__password)
        
user = User("Dave123")
user.show_password()
user.change_password("Tendo04")
user.show_password() 


# Exercise 2
class Server:
    def __init__(self, status):
        self.__status = status
        
    def start(self):
        print("The server is running")
        
    def stop(self):
        print("The server stopped running")
        
    def get_status(self):
        print(server1.__status)
        

server1 = Server("running")
server1.start()
server1.stop()
server1.get_status()


# exercise 3
class AI_Agent:
    def __init__(self, api_key):
        self.__api_key = api_key
        
    def update_key(self, api_key):
        self.__api_key = api_key
        
    def show_key(self):
        print(ai_agent1.__api_key)
        
             
ai_agent1 = AI_Agent("&5%$23@1456788908")
ai_agent1.update_key("&5%$23@@###@67755")
# print(ai_agent1.__api_key)
