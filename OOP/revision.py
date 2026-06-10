# I want to first go through what I have learnt so far 
# That is polymorphism and Inheritance
# Inheritance is a situation where someone adopts the characteristics of another person
# for example in Inheritance, a child can adopt the characters of the father ie his eyes, his legs, his skin tone
# Now in polymorphism

# Method overriding

# The Core Idea
# The parent class already has a method.
# The child class creates a method with the exact same name.
# Python uses the child's version instead of the parent's version.


# examples in Inheritance
# Revision on both Inheritance and polymorphism
class Parent():
    def __init__(self,name):
        self.name = name
        
    def introduce(self):
            print(f"My name is {self.name}")
        
        
class Child(Parent):
       pass
   
child1 = Child("Tendo Calvin")
child1.introduce()

