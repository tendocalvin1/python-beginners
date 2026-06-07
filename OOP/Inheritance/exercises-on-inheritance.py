
# Exercise 1: Animal Hierarchy
class Animal():
    def eat(self):
        print("The animal is eating")
        
    def sleep(self):
        print("The animal is sleeping")
        

class Dog(Animal):
    pass

dog1 = Dog()
dog1.eat()
dog1.sleep()

# Exercise 2: Person Hierarchy
class Person():
    def __init__(self, name):
        self.name = name
    
    def introduce(self):
        print(f"My name is {self.name}")
        
    # def name(self):
    #     print(f"My name is {self.name}")
        
        
class Teacher(Person):
    pass


teacher1 = Teacher("Boateng")

teacher1.introduce()


# Exercise 3: Vehicle Hierarchy
class Vehicle():
    
    def start(self):
        print("Vehicle started moving")
        
    def stop(self):
        print("Vehicle stopped moving")
        
        
        
class Motorcycle(Vehicle):
    pass


motorbike = Motorcycle()
motorbike.start()
motorbike.stop()


# Exercise 4: User System
class User():
    
    def login(self):
        print("Please login to access our system")
        
    def logout(self):
        print("Welcome, you can now log out")
        

class Customer(User):
    pass


customer1 = Customer()
customer1.login()
customer1.logout()

# Exercise 5: Bank System
class BankAccount():
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
        
        
class SavingsAccount(BankAccount):
    pass


savings1 = SavingsAccount("Tendo", 2000)
savings1.deposit(500)
savings1.withdraw(50)
savings1.display_balance()


# Exercise 6: Server Monitoring System
class Server():
    
    def start(self):
        print("The server has started")
        
    def stop(self):
        print("The server has stopped")
        
    def restart(self):
        print("The server is restarting")


class WebServer(Server):
    pass


web1 = WebServer()
web1.restart()
web1.start()
web1.stop()