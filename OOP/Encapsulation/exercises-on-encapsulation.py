
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
        self.__requests_remaining = 5
        
    def make_request(self):
        if self.__requests_remaining > 0:
            self.__requests_remaining -= 1
            print("Requests successful")
            
        else:
            print("No requests remaining")
            
    def show_remaining(self):
        print(self.__requests_remaining)
        
    
requests = RateLimiter(-1)
requests.make_request()
requests.show_remaining()


# Exercise 4: Server Monitoring
class Server:
    def __init__(self, cpu_usage):
        self.__cpu_usage = cpu_usage
        
        
    def increase_amount(self, amount):
        if self.__cpu_usage + amount <= 100:
            self.__cpu_usage += amount
        
        else:
            print("CPU usage cannot exceed 100")
                
    def decrease_usage(self, amount):
        if self.__cpu_usage - amount >= 0:
            self.__cpu_usage -= amount
            
        else:
            print("CPU usage cannot go below 0")
        
    
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
        if self.__memory_count > 0:
            self.__memory_count -= 1
        else:
            print("No memories to forget")
        
    def show_memory(self):
        print(self.__memory_count)
        

rag = AIAgent(100)
rag.remember()
rag.show_memory()

        
    
        
    