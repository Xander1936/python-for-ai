person = {
    "name": "Alice", "age": 30, "city": "New York"
}

person["name"] = "Bob"
person["licence"] = True  # Update the age
del person["licence"]

print(person.keys())
print(person.values())  
print(person.items())  

if "name" in person:
    print("Name is present in the dictionary")
    
person.update({"age": 31, "job": "Engineer"})  # Update multiple values
print(person)