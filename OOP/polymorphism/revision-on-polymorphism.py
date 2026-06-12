# The Core Definition
# Polymorphism means: Different objects can respond differently to the same method call.
# The method name is the same.
# The behavior is different.
# Polymorphism allows different objects to response differently to the same method call
# first python example demonstrating polymorphism
class Animal:
    def speak(self):
        pass
    
class Dog(Animal):
    def speak(self):
        print("Woof")
        
class Cat(Animal):
    def speak(self):
        print("Meow")
        
        
class Bird(Animal):
    def speak(self):
        print("Tweet")
        

dog = Dog()
cat = Cat()
bird = Bird()

cat.speak()
dog.speak()
bird.speak()


# 6 Examples of Polymorphism
# For each example, ask yourself: "How is the same method producing different behavior?"

# example 2
class Employee:
    def work(self):
        pass
    
class SoftwareEngineer(Employee):
    def work(self):
        print("Writing code")
        

class DataEngineer(Employee):
    def work(self):
        print("Building data pipelines")
        

class DevOpsEngineer(Employee):
    def work(self):
        print("Managing Infrastructure")
        
        
employees = [SoftwareEngineer(), DataEngineer(), DevOpsEngineer()]

for employee in employees:
    employee.work()
    
    
# Example 3: Servers (Systems Engineering)
class Server:
    def restart(self):
        pass
    
class WebServer(Server):
    def restart(self):
        print("Restarting Nginx")
        

class DatabaseServer(Server):
    def restart(self):
        print("Restarting PostgreSQL")
        
class CacheServer(Server):
    def restart(self):
        print("Restarting Redis")
        

servers = [WebServer(), DatabaseServer(), CacheServer()]

for server in servers:
    server.restart() 
    
    
# Example 4: AI Agent Tools
class Tool:
    def execute(self):
        pass
    
class SearchTool(Tool):
    def execute(self):
        print("Searching the web")
        
class EmailTool(Tool):
    def execute(self):
        print("Sending email")
        
class CalculatorTool(Tool):
    def execute(self):
        print("Performing calculations")
        

tools = [SearchTool(), EmailTool(), CalculatorTool()]

for tool in tools:
    tool.execute()


# Example 5: Notifications
class Notification:
    def send(self):
        pass
    
class EmailNotification(Notification):
    def send(self):
        print("Email sent")
        
class SMSNotification(Notification):
    def send(self):
        print("SMS sent")
        

class PushNotification(Notification):
    def send(self):
        print("Push Notification sent")
        

notifications = [EmailNotification(), SMSNotification(), PushNotification()]

for notification in notifications:
    notification.send()
  
  
# Example 6: Payment Systems
class Payment:
    def process(self):
        pass
    
    
class MobileMoney(Payment):
    def process(self):
        print("Processing Mobile Money transaction")


class CreditCard(Payment):
    def process(self):
        print("Processing Visa payment")
        
class PayPal(Payment):
    def process(self):
        print("Processing PayPal payment")
        
        
payments = [MobileMoney(), CreditCard(), PayPal()]

for payment in payments:
    payment.process()
