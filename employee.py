class Employee(object):

    def __init__(self, name, ID):
        
        self.name = name
        self.ID = ID

    def display(self):

        print(self.name)
        print(self.ID)

class Person(Employee):

    def __init__(self, name, ID, salary, post):

     self.salary = salary
     self.post = post

     Employee.__init__(self, name, ID)

a = Person('Rahul', 244243 , 20000, 'Intern')
a.display()

print(f"Salary: {a.salary}, Post: {a.post}")