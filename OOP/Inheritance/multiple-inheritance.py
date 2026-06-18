# Multiple Inheritance
# A class can inherit from more than one parent.

class SearchTool:
    def search(self):
        print("Searching...")
        
class MemoryTool:
    def remember(self):
        print("Remembering...")
        
class SmartAgent(SearchTool, MemoryTool):
    pass


agent = SmartAgent()
agent.remember()
agent.search()


class A:
    def greet(self):
        print("Hello from A")


class B:
    def greet(self):
        print("Hello from B")


class C(A, B):
    pass


person = C()
person.greet()

# Step 2: Understanding MRO
# When Python looks for a method, which class should it search first?

class Database:
    def connect(self):
        print("Database connection")


class Logger:
    def connect(self):
        print("Logging connection")


class PostgreSQL(Database, Logger):
    pass

db = PostgreSQL()
db.connect()