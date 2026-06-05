

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
        
    def study(self):
        print(f"{self.name} is studying {self.course}")
        
    def introduce(self):
        print(f"My name is {self.name}")