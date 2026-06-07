# Inheritance examples
# Example 1: Animal → Dog

class Animal():
    def eat(self):
        print("The animal is eating")
        

class Dog(Animal):
    pass

dog = Dog()
dog.eat()


# Example 2: Person → Student
class Person():
    def __init__(self, name):
        self.name = name
        
    def introduce(self):
        print(F"My name is {self.name}")
        
    
class Student(Person):
    pass


student = Student("Daniel Agger")
student.introduce()


# Example 3: Vehicle → Car
class Vehicle:
    def start(self):
        print("Vehicle started")


class Car(Vehicle):
    pass


car = Car()
car.start()


# Example 4: Employee → Manager
class Employee:
    def work(self):
        print("Employee working")


class Manager(Employee):
    pass


manager = Manager()

manager.work()


# Example 5: User → AdminUser
# This looks very similar to Django.

class User:
    def login(self):
        print("User logged in")


class AdminUser(User):
    pass

user = User()
user.login()
