# exercises on super(). __init__()

# number one


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    
class SoftwareEngineer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
         
        self.language = language
         

SWE = SoftwareEngineer("Tendo", '$100,000', "python")

print(SWE.name)
print(SWE.salary)


# exercise 2
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        

class Car(Vehicle):
    def __init__(self, brand, year, color):
        super().__init__(brand, year)
        
        self.color = color
        
        
car1 = Car("Tesla", 2026, "red")
print(car1.brand)
print(car1.year)
print(car1.color)




# exercise 3
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        
    
class AdminUser(User):
    def __init__(self, username, email, permissions):
        super().__init__(username, email)
        
        self.permissions = permissions
        
        
user1 = AdminUser("calvin6", "tendo@gmail.com", True)

print(user1.permissions)
print(user1.email)
print(user1.username)