# Empty tuple
empty = ()

# Tuple with items
point = (3, 5)
colors = ('red', 'green', 'blue')

# Single item tuple (needs the comma)
single = (42,) # Note the comma after 42
not_tuple = (42) # This is just an integer, not a tuple

# Without parentheses (tuple packing or implicit tuple)
coordinates = 10, 20 

colors[0]# This creates a tuple (10, 20, 30)
print(colors[-1])  # Output: red
print(point[1])  # Output: 5

# Slicing works too
print(colors[0:2])  # Output: ('red', 'green')