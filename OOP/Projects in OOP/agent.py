from abc import ABC, abstractmethod


class AgentTool(ABC):
    def __init__(self):
        self._usage_count = 0

    @abstractmethod
    def execute(self, query):
        pass

    def show_usage(self):
        print(f"Usage count: {self._usage_count}")


class SearchTool(AgentTool):
    def execute(self, query):
        self._usage_count += 1
        print(f"Searching for: {query}")


class WeatherTool(AgentTool):
    def execute(self, query):
        self._usage_count += 1
        print(f"Getting weather for: {query}")


class CalculatorTool(AgentTool):
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
            
agent = Agent("TendoGPT")

search = SearchTool()
weather = WeatherTool()
calculator = CalculatorTool()

agent.register_tool(search)
agent.register_tool(weather)
agent.register_tool(calculator)

agent.show_tools()

agent.run_all_tools("AI Agents")