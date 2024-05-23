# Variables and Datatypes

"""
Definition:

- A variable is a name that references a value in the computer's memory.
"""

# Syntax: variable_name = value
# string: A sequence of characters enclosed in single or double quotes
name = "Abiira Nathan"
# strings are immutable
# This means that the value of a string cannot be changed once it is created
# name[0] = "N"  # This will raise an error

# The variable `name` is assigned the value "Abiira Nathan"
print(name)

# The value of a variable can be changed
name = "Nathan Abiira"
print(name)

# int, float, string, boolean, list, tuple, dictionary, set and more.
age = 20  # int
print(age)

height = 5.8  # float
print(height)

is_student = True  # boolean
print(is_student)

users = ["Nathan", "John", "Jane"]  # list
print(users)

# for loop to iterate over the list of users
for user in users:
    print(user)


students = {"Joseph", "Jane", "John"}  # set
print(students)

# OR can be defined as a set using the set() function
students = set(["Joseph", "Jane", "John"])
print(students)


# A dictionary is a collection of key-value pairs
person = {"name": "Nathan", "age": 20, "is_student": True}
print(person)

# Accessing the value of a key in a dictionary
print(person["name"])  # Nathan
print(person["age"])  # 20
print(person["is_student"])  # True

# Adding a new key-value pair to a dictionary
person["height"] = 5.8
print(person)

# Removing a key-value pair from a dictionary
person.pop("is_student")  # or del person["is_student"]


# A tuple is a collection of items which is ordered and unchangeable
# Tuples are written with round brackets
coordinates = (4, 5)
print(coordinates)
print(coordinates[0])  # 4
print(coordinates[1])  # 5


# A tuple with one item should have a trailing comma
# Otherwise, it will be considered a string
single_item_tuple = ("apple",)
print(single_item_tuple)
