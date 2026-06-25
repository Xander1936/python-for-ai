# Pattern 1: Import the whole module
import math
# Now use: math.sqrt(16)

# Pattern 2: Import specific items from a module
from math import sqrt, pi
# Now use: sqrt(16)

# Import entire module
import random

# Use module functions
number = random.randint(1, 10)
choice = random.choice(["apple", "banana", "orange"])

# Date and time
import datetime
today = datetime.date.today()
print(today)  # 2024-01-15

# Operating system
import os
current_dir = os.getcwd()
print(current_dir)

# JSON data
import json
data = {"name": "Alice", "age": 30}
json_string = json.dumps(data)
print(json_string)

# Import entire module
import math
result = math.sqrt(16)
print(f"Square root of 16 is {result}")  # Square root of 16 is 4.0

# Import specific functions
from math import sqrt, pi
result = sqrt(16)
radius = 5
circle_area = pi * radius ** 2
print(f"Circle area: {circle_area}")  # Circle area: 78.53981633974483

# Import with alias
# import pandas as pd

# from pydantic import BaseModel
# df = pd.DataFrame(data)

# Import everything (avoid this!)
# from math import *

# Install a package
# pip install requests 

# Install specific version
# pip install requests==2.28.0

# Install multiple packages
# pip install pandas numpy matplotlib
