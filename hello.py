# import requests

# response = requests.get('https://api.github.com')
# print(response.status_code)
# print("Hello, World!")



first_name = "Alice"
last_name = "Smith"

full_name = first_name.lower() + " " + last_name.upper()
print(full_name)

long_dash = "-" * 12

print(long_dash)

user_age = 30

print(f"Hello, {first_name}! You are {user_age} years old.")
length_of_name = len(full_name)
print(f"Your full name has {length_of_name} characters.")

age = 30
has_license = True
drunk = True

can_drive = age >= 18 and has_license and not drunk
print(f"Can {first_name} drive? {can_drive}")

sentence = "hi my name is Dave"
sentence.title()

print("Hi" in sentence)
print(sentence.startswith("Hi"))
print(sentence.endswith("Dave"))

print(sentence.replace("Dave", "Alice"))
print(sentence.find("Dave"))
print(sentence.count("i"))