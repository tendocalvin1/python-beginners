# By this point, I have already seen:

# Inheritance → sharing behavior
# Polymorphism → same method, different behavior
# Encapsulation → protecting state

# Abstraction is different.

# Abstraction is about: Defining a contract that every child class must follow.

# Think of it as creating rules for future developers.


# Example 1: AI Agent Tools
# Imagine you're building your own AI framework.

from abc import ABC, abstractmethod
class Tool(ABC):
    @abstractmethod
    def execute(self):
        pass
    
    
class SearchTool(Tool):
    def execute(self):
        print("Searching the internet...")
        
class WeatherTool(Tool):
    def execute(self):
        print("Gathering weather information...")
        
        
tools = [SearchTool(), WeatherTool()]
for tool in tools:
    tool.execute()
    
# Example 2: Server Monitoring
from abc import ABC, abstractmethod

class Monitor(ABC):
    @abstractmethod
    def check_status(self):
        pass
    
class CPUMonitor(Monitor):
    def check_status(self):
        print("CPU usage: 35%")
        
class MemoryMonitor(Monitor):
    def check_status(self):
        print("RAM usage: 60%")
        
        
monitors = [CPUMonitor(), MemoryMonitor()]
for monitor in monitors:
    monitor.check_status()
    

# Example 3: Django-Inspired Views

# This one is very close to real Django.
from abc import ABC, abstractmethod
class View(ABC):
    @abstractmethod
    def get(self):
        pass
    

class ProductView(View):
    def get(self):
        print("Fetching products")
        
class UserView(View):
    def get(self):
        print("Fetching users")
        
views = [ProductView(), UserView()]

for view in views:
    view.get()
