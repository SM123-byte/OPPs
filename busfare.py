# Create Parent Class

class Vehicle:
    
    # Create a __init__ method 

    def __init__(self, fare_price, seating_capacity):

        self.fare_price = fare_price
        self.seating_capacity = seating_capacity
    
    # Create a method for calculating fare without maintenance charge 

    def calculate(self):
        return self.fare_price * self.seating_capacity

# Create a Child Class 

class Bus(Vehicle):

    # Create a __init__ method
    # Create a super().__init__ method for inheritance of Parent Class
    # Give value of maintenance charge

    def __init__(self, fare_price, seating_capacity, maintenance_charge = 0.10):
        super().__init__(fare_price, seating_capacity)
        self.maintenance_charge = maintenance_charge

    # Calculate full fare taking maintenance charge into account 

    def full_fare(self):
        fr = self.calculate()
        return fr + (fr * self.maintenance_charge)

# Object Creation
# Give values of fare price and seating capacity
# Print out values of full fare

bus = Bus(50, 100)
print(f"The total bus fare is {bus.full_fare()}")