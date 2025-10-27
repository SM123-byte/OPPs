class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

Bus1 = Bus("School Bus", 70, 12)
Car1 = Car("Audi", 230, 10)

print(f"Name: {Bus1.name}, Max Speed: {Bus1.max_speed}, Mileage: {Bus1.mileage}")
print(f"Name: {Car1.name}, Max Speed: {Car1.max_speed}, Mileage: {Car1.mileage}")