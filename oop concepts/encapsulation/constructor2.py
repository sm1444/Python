class Employee():
    name = None
    age = None
    salary = None

    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def getData(self):
        print("Name is : ",self.name)
        print("Age is: ",self.age)
        print("Salary is: ",self.salary)

emp1 = Employee("amit",20,10000)
emp1.getData()
emp2= Employee("rajesh",21,11000)
emp2.getData()