# print("Hello, World!")

temperature = 25

if temperature > 30:
    print("It's a hot day")
elif temperature < 10:
    print("It's a cold day")
else:
    print("It's a nice weather")
    
    
score = 90

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F - Need improvement")
    

# Nested if statements
has_ticket = True
age = 20
if has_ticket and age >= 18:
    print("You can enter the concert")
else:
    print("You cannot enter the concert")