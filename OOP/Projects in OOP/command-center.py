# Exercise 1: AI Agent Command Center ⭐
from abc import ABC, abstractmethod

class Tool(ABC):
    def __init__(self):
        self._usage_count = 0
    
    @abstractmethod
    def execute(self):
        pass
    
class SearchTool(Tool):
    def execute(self, query):
        self._usage_count += 1
        print(f"Searching for: {query}")
        

class WeatherTool(Tool):
    def execute(self, query):
        self._usage_count += 1
        print(f"Getting weather for: {query}")
        
class TranslationTool(Tool):
    def execute(self, query):
        self._usage_count += 1
        print(f"Calculating: {query}")
        

class Agent:
    def __init__(self, name):
        self.name = name
        self.tools = []
        
    def register_tool(self, tool):
        self.tools.append(tool)
        
        
    def show_tools(self):
        print(f"\n{self.name}'s Tools:")
        for tool in self.tools:
            print(tool.__class__.__name__)
            
            
    def run_all_tools(self, query):
        for tool in self.tools:
            tool.execute(query)
            
agent = Agent("ChatGPT")
            
google = SearchTool()
weather = WeatherTool()
langchain = TranslationTool()

agent.register_tool(google)
agent.register_tool(weather)
agent.register_tool(langchain)

agent.run_all_tools("Agents")