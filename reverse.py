# Create Class "Reverse"

class Reverse:

    # Create constructor for class

    def __init__(self):
        self.s = input("Enter a word: ")

    # Create method for reversing string

    def reverse_string(self):
        word = list(self.s)
        word.reverse()
        return "".join(word)

# Object Creation 

string_input = Reverse()
reversed_result = string_input.reverse_string()

# Printing Results 

print(f"Original Word: {string_input.s}")
print(f"Reversed Word: {reversed_result}")