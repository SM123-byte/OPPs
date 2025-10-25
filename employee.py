class Employee():

    def __init__(self):
        print("Employee created...")

    def __del__(self):
        print("Destructor called.")

def CreateObject():
    print("Making Object...")
    obj = Employee()
    print("Function End.")
    return obj

print("Calling create object")
obj1 = CreateObject()
print("Programme end.")