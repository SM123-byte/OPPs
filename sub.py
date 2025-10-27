class Vehicle:

    def __init__(vehicletype):
        print(f"Vehicle is a {vehicletype}")
    
class Car(Vehicle):

    def __init__(self):
        Vehicle.__init__('Car')

print(issubclass(Car, Vehicle))        
print(issubclass(Vehicle, Car))   
print(issubclass(Car, list))        
print(issubclass(Car, Car))       
print(issubclass(Car, (list, Vehicle)))        