class A:

    def __init__(self, a):
        self.a = a

    def __lt__(self, other):
        if self.a < other.a:
            return "obj 1 is less than obj 2"
        else:
            return "obj 2 is less than obj 1"
        
    def __eql__(self, other):
        if (self.a == other.a):
            return ("obj 1 is equal to obj 2")
        else:
            return ("Not equal")
        
ob1 = A(3)
ob2 = A(4)
print("Passed value:", ob1.a, ob2.a)

ob3 = A(6)
ob4 = A(6)
print("Passed value:", ob3.a, ob4.a)    

print(ob1 < ob2)
print(ob3 == ob4)