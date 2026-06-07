# use of the super() method in inheritance and in particular OOP

class Animal:
    def __init__(self, name):
        self.name = name
        
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        
dog = Dog("Roma", "German Shepherd")

print(dog.breed)
print(dog.name)

# Backend Engineering Example
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        
class AdminUser(User):
    def __init__(self, username, email, permissions):
        super().__init__(username, email)
        
        self.permissions = permissions
        
admin = AdminUser("Tendo", "tendo@gmail.com", ["delete_users"])

print(admin.username)
print(admin.email)
print(admin.permissions)
    
    
        