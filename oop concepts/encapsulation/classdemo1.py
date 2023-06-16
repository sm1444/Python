class Student:
    
    def getData(self):
       name = input("Enter your name: ")
       id = input("Enter your enrollment number: ")
       age= int(input("Enter you age: "))

    def display_data(self):
        print("---------------")
        print("Name: ",self.name)
        print("Enrollment number: ",self.id)
        print("Age: ",self.age)

stu = Student()
stu.getData()
stu.display_data()