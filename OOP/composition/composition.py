# Composition
# Composition examples to show difference between composition and inheritance
# composition helps in avoiding repetition compared to inheritance
class Engine:
    def start(self):
        print("Engine started")
        
class PetrolEngine(Engine):
    def start(self):
        print("Petrol engine started")


class ElectricEngine(Engine):
    def start(self):
        print("Electric engine started")
        
class Car:
    def __init__(self, engine):
        self.engine = engine
        
    def start(self):
        self.engine.start()
        print("Car moving")
    
# tesla = Car('')
# tesla.start()


# Why Composition Is Powerful

# Suppose tomorrow:
# PetrolEngine
# ElectricEngine
# HybridEngine

# You can swap engines.


        
tesla = Car(ElectricEngine())
toyota = Car(PetrolEngine())