# Now to understand polymorphism and how it works, I need to do some exercises so that
# the concept becomes second nature to me
# polymorphism is one of the important pillars of OOP
# Exercises on another pillar of OOP (Polymorphism)

# exercise one
class Vehicle:
    def move(self):
        pass
    
class Car(Vehicle):
    def move(self):
        print("A person drives a car on the road")
        
class Motorcycle(Vehicle):
    def move(self):
        print("A person rides a motorcycle on the road")
        
        
class Airplane(Vehicle):
    def move(self):
        print("The airplane is flying through the air")
        
        
vehicles = [Car(), Motorcycle(), Airplane()]

for vehicle in vehicles:
    vehicle.move()
    
    
    
# Exercise 2: Database Systems
class Database:
    def connect(self):
        pass
    
    
class PostgreSQL(Database):
    def connect(self):
        print("🐘 PostgreSQL: Establishing a secure pool connection on port 5432... Connected.")
        
        
class MySql(Database):
    def connect(self):
        print("🐬 MySQL: Initializing master-slave replication handshake on port 3306... Connected.")
        

class MongoDB(Database):
    def connect(self):
        print("🍃 MongoDB: Connecting to distributed cluster replica set... Connected.")
        

databases = [PostgreSQL(), MySql(), MongoDB()]

for database in databases:
    database.connect()
    
    
# Exercise 3: AI Agent Tools
class Tool:
    def execute(self):
        pass
    
class SearchTool(Tool):
    def execute(self):
        print("🔍 SearchTool: Querying index databases and ranking semantic results...")
        

class WeatherTool(Tool):
    def execute(self):
        print("🌤️  WeatherTool: Fetching real-time meteorological metrics and UV index...")
        
        
class TranslationTool(Tool):
    def execute(self):
        print("🌐 TranslationTool: Invoking multi-language neural machine translation model...")
        
        
# tools = [SearchTool(), WeatherTool(), TranslationTool()]
tools = [WeatherTool(), SearchTool(), TranslationTool()]

for tool in tools:
    tool.execute()
    
# Exercise 4: Monitoring Systems
class Monitor:
    def check_status(self):
        pass
    
class CPUMonitor(Monitor):
    def check_status(self):
        print("Checking CPU usage... Utilization is at 45%.") 
        
        
class MemoryMonitor(Monitor):
    def check_status(self):
        print("Checking RAM availability... 8GB out of 16GB used.") 
        
        
class DiskMonitor(Monitor):
    def check_status(self):
        print("Checking storage capacity... 120GB free on /dev/sda1.") 
        
monitors = [CPUMonitor(), MemoryMonitor(), DiskMonitor()]
for monitor in monitors:
    monitor.check_status()
    
    
# Exercise 5: Authentication System
class Authenticator:
    def login(self):
        pass
    
    
class GoogleLogin(Authenticator):
    def login(self):
        print("Logging in with Google... Redirecting to OAuth.")
        
        
class GitHubLogin(Authenticator):
    def login(self):
        print("Logging in with GitHub... Fetching user scopes.")
        
        
class LinkedInLogin(Authenticator):
    def login(self):
        print("Logging in with LinkedIn... Initializing handshake.")
        
        
authenticators = [GoogleLogin(), GitHubLogin(), LinkedInLogin()]
for authenticator in authenticators:
    authenticator.login()
    
    
# Exercise 6: Django-Inspired Views
class View:
    def get(self):
        pass
    
class ProductView(View):
    def get(self):
        print("Fetching product catalog from database... Status: 200 OK")
        
class UserView(View):
    def get(self):
        print("Retrieving user profile info... Status: 200 OK")
        
        
class OrderView(View):
    def get(self):
        print("Processing order history logs... Status: 200 OK")
        
        
views = [ProductView(), UserView(), OrderView()]
for view in views:
    view.get()