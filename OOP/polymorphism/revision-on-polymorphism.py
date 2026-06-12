# The Core Definition
# Polymorphism means: Different objects can respond differently to the same method call.
# The method name is the same.
# The behavior is different.

# first python example demonstrating polymorphism
class Animal:
    def speak(self):
        pass
    
class Dog(Animal):
    def speak(self):
        print("Woof")
        
class Cat(Animal):
    def speak(self):
        print("Meow")
        
        
class Bird(Animal):
    def speak(self):
        print("Tweet")
        

dog = Dog()
cat = Cat()
bird = Bird()

cat.speak()
dog.speak()
bird.speak()


# 6 Examples of Polymorphism
# For each example, ask yourself: "How is the same method producing different behavior?"

# example 2
