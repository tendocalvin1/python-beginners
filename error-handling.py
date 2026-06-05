# Error Handling (try and except)

number = int(input("Enter an interger: "))
print(number)

# With Error Handling
try:
    number = int("hello")
    
except ValueError:
    print("Please enter a valid number")
    
    
# try:
#     result = 10 / 0
#     print(result)
    
# except ValueError:
#     print("Cannot divide by zero")
    
# The else Block
try:
    number = int("10")

except ValueError:
    print("Error")

else:
    print("Everything worked")
    
# The finally Block
# Always runs without fail
try:
    print("Trying")

except:
    print("Error")

finally:
    print("Always runs")
    
    
# try:
#     print(user[age])
    
# except KeyError:
#     print("Age not found")
