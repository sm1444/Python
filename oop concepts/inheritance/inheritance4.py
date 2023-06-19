#multiple inheritance --- many parent class single child class
class Diwali():
    
    crackers = 100
    holidays = 5
    def __init__(self):
        print("diwali constructor")          

class Holi():
    balloons = 120
    holidays = 2
    def __init__(self):
        print("holi constructor")


class Festival(Holi,Diwali):
    def __init__(self):
        super().__init__()
        print("festival constructor")
        
    
    def celebrate(self):
        print("celebrating festival")
        print("crackers: ", self.crackers)
        print("balloons: ", self.balloons)
        print("holidays: ", self.holidays)  

f = Festival()
f.celebrate()  

#the constructor and the property having same name is called in child class as per the declaration of parent class in child class parameter