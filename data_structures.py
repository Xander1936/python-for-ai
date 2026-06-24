age = 25
has_license = False

my_list = ["Alice", 25, age, True, has_license]

name = my_list[0]
my_list[0] = "Dave"
age_from_list = my_list[1]

has_license_from_list = my_list[4]

my_list.append("Smith")
my_list.remove("Dave")
my_list.insert(1, "Bob")
print(my_list)