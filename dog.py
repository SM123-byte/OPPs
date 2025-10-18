# A program for the class of Dogs

class Dog:

# Declaration of Instance Attributes

    def __init__(self, colour, breed):
        self.colour = colour
        self.breed = breed
        
# Object Creation of Dogs

Barney = Dog("grey", "Great Dane")
Max = Dog("white", "Poodle")

# Display colour of dogs

print(f"Barney's coat colour is {Barney.colour}")
print(f"Max's coat colour is {Max.colour}")

# Display breed of dogs

print(f"Barney's breed is the {Barney.breed}")
print(f"Max's breed is the {Max.breed}")