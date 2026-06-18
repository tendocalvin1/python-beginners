from abc import ABC, abstractmethod

class Monitor(ABC):
    def __init__(self, current_value):
        self._current_value = current_value
        
    @abstractmethod
    def check_status(self):
        pass
    
class CPUMonitor(Monitor):
    def check_status(self):
        print(f"CPU Usage is currently at {self._current_value}%")

class MemoryMonitor(Monitor):
    def check_status(self):
        print(f"Memory Available RAM is at {self._current_value} GB")

class DiskMonitor(Monitor):
    def check_status(self):
        print(f"Disk Storage space utilized: {self._current_value}%")

class NetworkMonitor(Monitor):
    def check_status(self):
        print(f"Network Current latency: {self._current_value}ms")


class MonitoringSystem:
    def __init__(self, name):
        self.name = name
        self.monitors = [] 
        
    def add_monitor(self, monitor: Monitor):
        self.monitors.append(monitor)
        print(f"[System] Successfully registered {monitor.__class__.__name__}")
    
    def show_monitors(self):
        print(f"\n--- Registered Monitors for {self.name} ---")
        for m in self.monitors:
            print(f" - {m.__class__.__name__}")
    
    def run_health_check(self):
        print(f"\n--- Running Global Health Check for {self.name} ---")
        for monitor in self.monitors:
            monitor.check_status()
        print("--- Health Check Complete ---\n")


cpu = CPUMonitor(45)
memory = MemoryMonitor(16)
disk = DiskMonitor(60)
network = NetworkMonitor(12)


system = MonitoringSystem("Production_Server")


system.add_monitor(cpu)
system.add_monitor(memory)
system.add_monitor(disk)
system.add_monitor(network)


system.show_monitors()
system.run_health_check()