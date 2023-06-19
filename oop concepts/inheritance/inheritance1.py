#single inheritance a-->b

class Phone():
    model=""   #class variable/instance variable
    makeyear=""
    def phoneData(self):
        print("Phone Data")
    
    def __init__(self):   #it is given priority and called directly through child class object only when there is no child class constructor , if child class constructor is present then it is not called unlike Java and c++
        print("Parent class constructor")

class Apple(Phone):
    #def __init__(self):
    #     super().__init__() #calling parent class constructor
    #     print("Child class constructor")

    def getPhoneData(self):
        self.model=input("Enter phone model: ")
        self.makeyear=input("Enter make year: ")

    def printData(self):
        print("Model: ",self.model)
        print("Make year: ",self.makeyear)

phone = Apple()
phone.getPhoneData()
phone.printData()