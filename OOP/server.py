

class Server():
    def __init__(self, hostname, ip_address, status):
        self.hostname = hostname
        self.ip_address = ip_address
        self.status = status
        
    def start(self):
        print(f"{self.hostname} is {self.status}")
        
    def stop(self):
        print(f"{self.hostname} has {self.status} running")
        
        
    def restart(self):
        print(f"{self.hostname} has {self.status}")