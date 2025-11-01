class myClass:

    # Private variable 

    __pri = 27;

    def __PriMethod(self):
        print("I'm inside class myClass");
    
    def hello(self):
        print("Private variable value:",myClass.__pri)

foo = myClass()
foo.hello()
foo.__PriMethod