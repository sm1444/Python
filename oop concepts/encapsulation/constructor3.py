#iterating object in a class using object list to avoid creating seperate objects each time

class emp():
    name = None
    def __init__(self,name):
        self.name = name

    def printName(self):
        print("Name is: ",self.name)

object_list = []
for i in range(3):
    user_name = emp(input("Enter name: "))
    object_list.append(user_name)

for i in object_list:
    i.printName()
