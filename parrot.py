class Parrot:

    # Class Attribute 

    species = "bird"

    # Instance Attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age

blu = Parrot("Blu", 10)
woo = Parrot("Woo", 13)

print(f"Blu is a {blu.species}.")
print(f"Woo is also a {woo.species}.")

print(f"Blu is {blu.age}.")
print(f"Woo is {woo.age}.")