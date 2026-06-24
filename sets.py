# Empty set(careful, this is not the same as an empty dictionary)
empty_set = set() # NOT {} which is an empty dictionary

# Set with values  - both ways of creating a set are valid
numbers = {1, 2, 3, 4, 5}
fruits = set(['apple', 'banana', 'cherry'])

# From a list (removes duplicates values)
scores = [90, 80, 70, 90, 80]
unique_scores = set(scores) # {70, 80, 90}

print(unique_scores) # Output: {70, 80, 90}