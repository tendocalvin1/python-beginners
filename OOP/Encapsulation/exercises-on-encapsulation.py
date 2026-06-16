
# number one
class SocialMediaAccount:
    def __init__(self, followers):
        self.__followers = followers
        
    def follow(self):
        self.__followers += 1
        
    def unfollow(self):
        self.__followers -= 1
        
    def show_followers(self):
        print(self.__followers)
        
        
instagram = SocialMediaAccount(100)
instagram.follow()
instagram.show_followers()
instagram.unfollow()
instagram.show_followers()


# Exercise 2: Database Connection
class DatabaseConnection:
    def __init__(self, connected):
        self.__connected = connected
        
    def connect(self):
        self.__connected = True
        
    def disconnect(self):
        self.__connected = False
        
    def status(self):
        print(self.__connected)
        
        
postgreSQL = DatabaseConnection("False")
postgreSQL.connect()
postgreSQL.status()
postgreSQL.disconnect()
postgreSQL.status()

# Exercise 3: API Rate Limiter
# Very useful for backend engineering.

class RateLimiter:
    def __init__(self, requests_remaining):
        self.__requests_remaining = requests_remaining
        
    def make_request(self):
        self.__requests_remaining -= 1
        
        if self.__requests_remaining < 0:
            print("Requests cannot be less than zero")
            
        # else:
        #     print("Invalid request")
            
    def show_remaining(self):
        print(self.__requests_remaining)
        
    
requests = RateLimiter(-1)
requests.make_request()
requests.show_remaining()


# Exercise 4: Server Monitoring
class Server:
    def __init__(self, cpu_usage):
        self.__cpu_usage = cpu_usage
        
        if (self.__cpu_usage >= 0 and  100):
            print("This is a valid value")
            
        else:
            print("Invalid valid, out of range!")
        
    def increase_amount(self, amount):
        self.__cpu_usage  += 1
        
    def decrease_usage(self, amount):
        self.__cpu_usage -= 1
        
    
    def show_usage(self):
        print(self.__cpu_usage)
        
web1 = Server(105)
web1.show_usage()


# Exercise 5: AI Agent Memory
class AIAgent:
    def __init__(self, memory_count):
        self.__memory_count = memory_count
        
    def remember(self):
        self.__memory_count += 1
        
    def forget(self):
        self.__memory_count -= 1
        
    def show_memory(self):
        print(self.__memory_count)
        

rag = AIAgent(100)
rag.remember()
rag.show_memory()
        
    
        
    