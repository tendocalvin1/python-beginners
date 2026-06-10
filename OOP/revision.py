# I want to first go through what I have learnt so far 
# That is polymorphism and Inheritance
# Inheritance is a situation where someone adopts the characteristics of another person
# for example in Inheritance, a child can adopt the characters of the father ie his eyes, his legs, his skin tone
# Now in polymorphism

# Method overriding

# The Core Idea
# The parent class already has a method.
# The child class creates a method with the exact same name.
# Python uses the child's version instead of the parent's version.


# examples in Inheritance
# Revision on both Inheritance and polymorphism
class Parent():
    def __init__(self,name):
        self.name = name
        
    def introduce(self):
            print(f"My name is {self.name}")
        
        
class Child(Parent):
       pass
   
child1 = Child("Tendo Calvin")
child1.introduce()



# class Vehicle:
#     def __init__(self, brand, name, year):
#         self.brand = brand
#         self.name = name
#         self.year = year
        
#     def start(self):
#         print("The vehicle has started moving")
        
#     def stop(self):
#         print("The vehicle has stopped moving")
        
    
# class Car(Vehicle):
#     pass

# car1 = Car("Tesla SUV","Model 2026", 2026)
# car1.start()
# car1.stop()

# print(car1.year)

# exercise number one
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def display_info(self):
        print(f"My name is {self.name} and my salary is ${self.salary}")
        

class SoftwareEngineer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name,salary)
        
        self.programming_language = programming_language
        
engineer1 = SoftwareEngineer("Tendo Calvin", 95000, "Python & JavaScript")
engineer1.display_info()


# Exercise 2: Server Infrastructure
class Server:
    def __init__(self, hostname, ip_address):
        self.hostname = hostname
        self.ip_address = ip_address
        
    
    def start(self):
        print("The server has started running")
        
    def stop(self):
        print("The server has stopped running")
        
    
class WebServer(Server):
    def __init__(self, hostname, ip_address, domain_name):
         super().__init__(hostname, ip_address)
         
         self.domain_name = domain_name
         
web1 = WebServer("acardia.com", 192.168, "DNS")
web1.stop()
web1.start()

print(web1.ip_address)
print(web1.hostname)
print(web1.domain_name)


# Exercise 3: AI Agent Tools
class Tool:
    def __init__(self, name, description):
         self.name = name
         self.description = description
         
    def show_info(self):
        print(f"The tool is called {self.name} and it does help with {self.description}")
        
    

class SearchTool(Tool):
    def __init__(self, name, description, search_engine):
        super().__init__(name, description)
        
        self.search_engine = search_engine
        
google_tool = SearchTool("Codex", "AI Powered assistance", "Chat GPT")
google_tool.show_info()


# Exercise 4: Banking System

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}")

    def display_balance(self):
        print(f"Current balance: {self.balance}")


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest added: {interest}")


# Create account
account = SavingsAccount("Tendo", 2000, 0.05)

# Perform operations
account.deposit(500)
account.withdraw(300)
account.apply_interest()
account.display_balance()  
        
