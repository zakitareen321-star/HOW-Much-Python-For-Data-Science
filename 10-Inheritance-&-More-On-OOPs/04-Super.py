# Sometime we want to run Employee constructor in Manager constructor then we use Super()._init_()

class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a=1

class programmer(Employee):
     def __init__(self):
        # super().__init__()      # If you want to display the Employee class in the Programmer class, uncomment this.
        print("This Inheritance show the Constractor of Programmer")
        
     b = 2
   

class Manager(programmer):
     def __init__(self):
        super().__init__()
        print("Constructor of Manager")
     c = 3
   


# o=Employee()         ## Uncomment one by one
# print(o.a)   # print The Attribute


# o=programmer()      ## Uncomment one by one
# print(o.a,o.b)

o=Manager()           
print(o.a,o.b,o.c)



## If you want the previous constructor’s behavior to be included in this constructor too, use the `super()` method.