# Import Math for Pi

import math

# Create class of Circle

class Circle:

    # Constructor Method

    def __init__(self):
        self.radius = (float(input("Enter the radius of the circle: ")))

    # Perimeter Function 

    def perimeter(self):
        return 2 * math.pi * self.radius
    
    # Area Function

    def area(self):
        return math.pi * self.radius ** 2

# Make Instance Variables     

circle = Circle()

perimeter = circle.perimeter()
area = circle.area()

# Print the outcome 

print(f"The circumference of the circle is {perimeter}")
print("The area of the circle is {area}")    