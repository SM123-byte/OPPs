class Vehicle:

    def __init__(self, name, mileage, max_speed):
        self.name = name
        self.mileage = mileage
        self.max_speed = max_speed

model1 = Vehicle("Audi", 13, 270)

print(f"Model Name: {model1.name} ")
print(f"Mileage: {model1.mileage}")
print(f"Max Speed: {model1.max_speed}")