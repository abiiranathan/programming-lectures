# Introduction to Python Classes

# ## Fundamentals of Classes in Python

# ### What is a Class?
# A class is a blueprint for creating objects. Classes encapsulate data for the object and methods to manipulate that data.

# ### Defining a Class
# We use the `class` keyword to define a class.


# Example:
class Dog:
    # Class attribute
    species = "Canis familiaris"

    # Initializer(constructor) / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age


# ### Creating an Instance
# An instance is a specific object created from a particular class.

# Example:
my_dog = Dog(name="Buddy", age=5)
print(my_dog.name)  # Output: Buddy
print(my_dog.age)  # Output: 5

# ## Instance Methods
# Methods that operate on instances of the class. They can access and modify the object’s attributes.


# Example:
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"


# Creating a new instance
my_dog = Dog(name="Buddy", age=5)

# Calling instance methods
print(my_dog.description())  # Output: Buddy is 5 years old
print(my_dog.speak("Woof Woof"))  # Output: Buddy says Woof Woof

# ## Class and Static Methods
# Class methods are methods that operate on the class itself rather than on instances of the class.
# Static methods don't operate on the instance or the class; they are like regular functions but belong to the class's namespace.


# Example:
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

    # Class method
    @classmethod
    def common_species(cls):
        return cls.species

    # Static method
    @staticmethod
    def bark():
        return "Woof Woof"


print(Dog.common_species())  # Output: Canis familiaris
print(Dog.bark())  # Output: Woof Woof

# ## Inheritance
# Inheritance allows us to define a class that inherits all the methods and properties from another class.


# Example:
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


# Child class (inherits from Dog)
class GoldenRetriever(Dog):
    def speak(self, sound="Woof"):
        return f"{self.name} says {sound} (happily)"


# Creating an instance of the child class
golden = GoldenRetriever(name="Max", age=3)

# Calling the inherited method
print(golden.description())  # Output: Max is 3 years old

# Calling the overridden method
print(golden.speak())  # Output: Max says Woof (happily)

# ## Polymorphism
# Polymorphism means "many forms." In Python, it allows us to perform the same action in different ways.


# Example:
class Dog:
    def speak(self):
        return "Woof"


class Cat:
    def speak(self):
        return "Meow"


# Creating instances of different classes
dog = Dog()
cat = Cat()

# Polymorphism in action
for animal in [dog, cat]:
    print(animal.speak())

# ## Abstraction
# Abstraction hides the implementation details and only shows the essential features of an object.

# Example:
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof"


class Cat(Animal):
    def speak(self):
        return "Meow"


# Creating instances of concrete classes
dog = Dog()
cat = Cat()

# Accessing the abstract method
print(dog.speak())  # Output: Woof
print(cat.speak())  # Output: Meow

# ## Encapsulation
# Encapsulation hides data and methods within a class, protecting them from direct access.


# Example:
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance


# Creating an instance of the BankAccount class
account = BankAccount(1000)

# Trying to access the private attribute directly (will raise an AttributeError)
# print(account.__balance)  # AttributeError: private access

# Accessing the attribute using public methods
account.deposit(500)
print(account.get_balance())  # Output: 1500
account.withdraw(200)
print(account.get_balance())  # Output: 1300

# ## Special Methods (Dunder Methods)
# Special methods in Python are denoted by double underscores (`__`) and are used for defining how objects behave in specific scenarios.


# Example:
class Dog:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"This is a dog named {self.name}"

    def __repr__(self) -> str:
        return f"Dog('{self.name}')"

    def __len__(self):
        return len(self.name)


# Creating an instance
my_dog = Dog("Buddy")

# Using the special methods
print(my_dog)  # Output: This is a dog named Buddy
print(len(my_dog))  # Output: 5

# ## Advanced Class Concepts

# ### Metaclasses
# Metaclasses control the creation of classes themselves. They allow you to customize the behavior of classes during their creation.


# Example:
class MyMeta(type):
    def __new__(cls, name, bases, attrs):
        attrs["my_attribute"] = "This is a metaclass attribute"
        return super().__new__(cls, name, bases, attrs)


class MyClass(metaclass=MyMeta):
    pass


print(MyClass.my_attribute)  # Output: This is a metaclass attribute

# ### Decorators for Classes
# Decorators can be applied to classes as well, providing a way to modify the behavior of a class without changing its code directly.


# Example:
def add_method(cls):
    def new_method(self):
        return "This is a new method"

    setattr(cls, "new_method", new_method)
    return cls


@add_method
class MyClass:
    pass


my_object = MyClass()
print(my_object.new_method())  # Output: This is a new method

# ### Class Properties
# Properties allow you to control access to class attributes, often used for data validation or to manage complex attributes.


# Example:
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = value


# Creating an instance and setting the salary
employee = Employee("Alice", 50000)

# Accessing the salary property
print(employee.salary)  # Output: 50000

# Trying to set an invalid salary
try:
    employee.salary = -1000
except ValueError as e:
    print(e)  # Output: Salary cannot be negative

# ## Example: Implementing a Simple Game

# Let's implement a simple text-based game using classes to demonstrate the concepts learned.

import random


class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage

    def attack_enemy(self, enemy):
        enemy.take_damage(self.attack)
        print(f"{self.name} attacks {enemy.name} for {self.attack} damage.")


class Enemy(Character):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)


class Player(Character):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)


def main():
    player_name = input("Enter your character name: ")
    player = Player(player_name, 100, 20)

    enemy = Enemy("Goblin", 50, 10)

    while player.is_alive() and enemy.is_alive():
        print("\n--- Turn ---")
        print(f"Player: {player.health} HP")
        print(f"Enemy: {enemy.health} HP")

        action = input("Attack (a) or Heal (h): ").lower()

        if action == "a":
            player.attack_enemy(enemy)
        elif action == "h":
            player.health += 10
            print(f"{player.name} heals for 10 HP.")
        else:
            print("Invalid action.")

        if enemy.is_alive():
            enemy.attack_enemy(player)

    if player.is_alive():
        print("\nYou have defeated the Goblin!")
    else:
        print("\nYou have been defeated.")


if __name__ == "__main__":
    main()
