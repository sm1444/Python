class Shape():
    name = None
    size=None
    def __init__(self,name,size):
        self.name= name
        self.size = size

    def getdata(self):
        print("Shape is: ",self.name)
        print(self.name," is of size ",self.size)

circle =  Shape("circle",20)
circle.getdata()
triangle = Shape("triangle",30)
triangle.getdata()