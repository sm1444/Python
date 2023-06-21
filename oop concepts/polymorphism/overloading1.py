class Parameter():
    def pop(self,param1,param2):
        print("pop with 2 parameters....",param1,param2)

    def pop(self):
        print("pop without parameter called...")

    def pop(self,param1):
        print("pop with 1 parameter called....",param1)

p = Parameter()
p.pop(12)  # the pop function which is declared last is executed 