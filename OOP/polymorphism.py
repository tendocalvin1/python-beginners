# Method overriding

# The Core Idea
# The parent class already has a method.
# The child class creates a method with the exact same name.
# Python uses the child's version instead of the parent's version.

# example 1
class Animal:
    def speak(self):
        print("The animal makes a sound")
        
class Dog(Animal):
    def speak(self):
        print("WOOF!")
        
        
dog = Dog()
dog.speak()


# example 2
class Vehicle:
    def start(self):
        print("Vehic;e started!")
        
        
class Car(Vehicle):
    def start(self):
        print("Tesla started silently")
        
        
car = Car()
car.start()


# The Most Important Pattern

# Often we don't want to completely replace the parent method.

# We want:
# Parent behavior
# +
# Child behavior

# This is where overriding and super() work together.

class Employee:
    def work(self):
        print("Employee working")
        
class SoftwareEngineer(Employee):
    def work(self):
        super().work()
        print("Writing python code")
        
    
engineer = SoftwareEngineer()
engineer.work()


# Systems Engineering Example
class Server:
    def start(self):
        print("Starting server")
        
        
class WebServer(Server):
    def start(self):
        super().start()
        print("Loading web services")
        
web1 = WebServer()
web1.start()


# exercises on method overriding
# exercise 1
class Animal:
    def speak(self):
        print("Meow!")
        
class Cat(Animal):
    def speak(self):
        super().speak()
        print("The animal is sneezing")
        
cat1 = Cat()
cat1.speak()

# exercise 2
class Employee:
    def work(self):
        print("Employee working")
        
class SoftwareEngineer(Employee):
    def work(self):
        super().work()
        print("Writing python applications")
        
        
swe = SoftwareEngineer()
swe.work()


# exercise 3
class Vehicle:
    def start(self):
        print("Vehicle starting")
        

class Car(Vehicle):
    def start(self):
        super().start()
        print("Tesla systems online")
        

tesla = Car()
tesla.start()

# Exercise 4
class User:
    def login(self):
        print("User logged in")
        

class AdminUser(User):
    def login(self):
        super().login()
        print("Admin dashboard loaded")
        

user = AdminUser()
user.login()


# exercise 5
class Server:
    def restart(self):
        print("Server restarting")
        
class WebServer(Server):
    def restart(self):
        super().restart()
        print("Reloading web applications")
        
web01 = WebServer()
web01.restart()
    