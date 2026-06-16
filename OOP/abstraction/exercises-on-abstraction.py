
# Exercise 1: Payment System
from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self):
        pass
    
class CreditCardPayment(PaymentMethod):
    def pay(self, amount: float):
        print(f"💳 Processing credit card payment of UGX {amount:,.0f}...")
        print("✅ Credit card payment successful!")
        

class MobileMoneyPayment(PaymentMethod):
    def pay(self, amount: float):
        print(f"📱 Initiating Mobile Money payment of UGX {amount:,.0f}...")
        print("✅ Mobile Money payment successful! Check your phone for confirmation.")
        
payments = [CreditCardPayment(), MobileMoneyPayment()]
for payment in payments:
    payment.pay(50000.0)
    
    
# Exercise 2: Database Systems
from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass
    
class PostgreSQL(Database):
    def connect(self):
        print("🐘 Connecting to PostgreSQL on localhost:5432...")
        print("✅ PostgreSQL connected! Database: myapp_db")
        

class MongoDB(Database):
    def connect(self):
        print("🍃 Connecting to MongoDB on localhost:27017...")
        print("✅ MongoDB connected! Cluster: myapp-cluster")
        
databases = [PostgreSQL(), MongoDB()]
for database in databases:
    database.connect()
    
    
# Exercise 3: AI Agent Framework
from abc import ABC, abstractmethod
import ast

class AgentTool(ABC):
    @abstractmethod
    def execute(self, query: str) -> str:
        pass
    
class SearchTool(AgentTool):
    def execute(self, query: str) -> str:
        print(f"🔍 Searching the web for: '{query}'...")
        print("✅ Found 10 results. Top result: 'Wikipedia - Artificial Intelligence'")
        return f"search_results_for:{query}"

class CalculatorTool(AgentTool):
    def execute(self, query: str) -> str:
        try:
            result = ast.literal_eval(query)  # ✅ safe — no code execution
            print(f"🧮 Evaluating expression: '{query}'...")
            print(f"✅ Result: {result}")
            return str(result)
        except (ValueError, SyntaxError):
            print(f"❌ Invalid expression: '{query}'")
            return "error:invalid_expression"

# Fix the routing — don't send "AI agents" to a calculator
search_tool = SearchTool()
calc_tool = CalculatorTool()

search_tool.execute("AI agents")
calc_tool.execute("100 + 250")  