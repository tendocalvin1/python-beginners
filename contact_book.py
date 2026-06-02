
numbers = {
    "Tendo": '256-777-7777',
    "Kendo": '256-777-7778',
    "Karen": '256-777-4545',
    "Maria": '256-705-6734'
}

print(numbers.get("Maria"))

keys = numbers.keys()
print(keys)

values = numbers.values()
print(values)

for key, value in numbers.items():
    print(f"{key} : {value}")
    
print(numbers.keys())
print(type(numbers.keys()))