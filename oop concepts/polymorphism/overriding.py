#overriding- parent class method created in child class with same signature is called method overriding

class Gov():
     def taxBody(self):
          print("Tax body is GST")

class Person(Gov):
     def taxBody(self):
          super().taxBody()
          print("tax body is income tax")

p = Person()
p.taxBody()