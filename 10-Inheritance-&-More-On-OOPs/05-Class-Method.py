class Employee:
    a=1
    
    @classmethod
    def show(cls):                                  # cls refers to the class itself and its own value.
      print(f"The class attribute of a is {cls.a}")

e=Employee()

e.show()   # Function call


# cls writes its own attribute.
# self first accesses the attributes of the current "instance/object.”.