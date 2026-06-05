# Object Oriented Programming in Python
# object = A "bundle" of related attributes(variables) and methods(functions)
#           Example : phone, cup, book
#           You need a class to create many objects

# class = A class is a blueprint used to design the structure and layout of an object

from car import Car
        
car1 = Car("Mustang", 2026, "red", False)
car2 = Car("Tesla", 2026, "black", True)


car1.drive()
car1.stop()
car1.describe()

print(car2.color)
print(car2.model)
print(car2.for_sale)
print(car2.year)