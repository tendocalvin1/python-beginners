# Project 1: AI Agent Framework

from abc import ABC, abstractmethod
import ast


class AgentTool(ABC):
    def __init__(self):
        self._usage_count = 0
    @abstractmethod
    def execute(self, query: str) -> str:
        pass
    
class SearchTool(AgentTool):
    def execute(self,query: str) -> str:
        self._usage_count += 1
        print(f"🔍 Searching the web for: '{query}'...")
        print("✅ Found 10 results. Top result: 'Wikipedia - Artificial Intelligence'")
        return f"search_results_for:{query}"
        
        
class CalculatorTool(AgentTool):
    def execute(self, query: str) -> str:
        self._usage_count += 1
        try:
            result = ast.literal_eval(query)  
            print(f"🧮 Evaluating expression: '{query}'...")
            print(f"✅ Result: {result}")
            return str(result)
        except (ValueError, SyntaxError):
            print(f"❌ Invalid expression: '{query}'")
            return "error:invalid_expression"
        
        
class WeatherTool(AgentTool):
    def execute(self,query: str) -> str:
        self._usage_count += 1
        print("Gathering weather information...")
        
        
class TranslationTool(AgentTool):
    def execute(self,query: str) -> str:
        self._usage_count += 1
        print("Translating computer language into machine language")

        
class DatabaseTool(AgentTool):
    def execute(self,query: str) -> str:
        self._usage_count += 1
        print("🐘 Connecting to PostgreSQL on localhost:5432...")
        print("✅ PostgreSQL connected! Database: myapp_db")
        
        
tools = [SearchTool(), CalculatorTool(), WeatherTool(), TranslationTool(), DatabaseTool()]
for tool in tools:
    tool.execute("AIAgents")

# google = SearchTool()
# google.execute("AI Agent")

# calculator = CalculatorTool()
# calculator.execute("5 + 39")

# weather = WeatherTool()
# weather.execute()

# translator = TranslationTool()
# translator.execute()
   
# database = DatabaseTool()
# database.execute() 
        