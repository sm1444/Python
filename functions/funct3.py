def students(x,*args):  # data type of args is tuple
    print(x)
    print(args)
    print(type(args))

students(100,200,300)

def students2(a,**kwargs): #Kwargs stores data in key value pair and its return type is dictionary
    print(kwargs)
    print(a)

students2(10,name="Shalvi",age=19)
