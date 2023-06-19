# multilevel inheritance a-->b-->c

class Gov():
    print("This is government class")
    tax = 12
    def __init__(self):
        print("This is gov class constructor ...")

class State(Gov):
    print("This is state class")
    grant = 10000
    def __init__(self):
        print("This is state class constructor...")
    def stateData(self):
        print("This is state class data function.")
        print("Tax= ",self.tax)
        print("Grant= ",self.grant)

class City(State):
    print("This is city class.")
    amount = 1000
    def __init__(self):
        print("This is city class constructor...")
    def cityData(self):
        print("This is city class data method")
        print("Tax= ",self.tax)
        print("Grant= ",self.grant)
        print("Amount= ",self.amount)

#city = City()  #default constructor #if city class constructor is not present state class constructor is called and if that is also not present then gov class constructor will be called
#city.cityData()
#city.stateData()

s = State()
s.stateData()
#s.cityData()  #error