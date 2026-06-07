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

# Systems Engineering Example

# Imagine monitoring servers.

class Server:
    def __init__(self, hostname, ip_address):
        self.hostname = hostname
        self.ip_address = ip_address
        
class WebServer(Server):
    def __init__(self, hostname, ip_address, domain):
        super().__init__(hostname, ip_address)
        
        self.domain = domain
        
web = WebServer("server01","192.168.1.1","example.com")

print(web.domain)
print(web.hostname)
print(web.ip_address)
    
        