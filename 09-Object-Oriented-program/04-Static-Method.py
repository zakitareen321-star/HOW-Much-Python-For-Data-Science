# Using @static method 

class Employee:
    language="Python"   
    Salary="150000$"

    
    def getinfo(self):
        print(f"The language is {self.language}. and the Salary is {self.Salary}")

    @staticmethod                      # This is called decorator in python
    def greet():
        print("Hello")       # we don't need any self object due to @static method 

    @staticmethod
    def company():
        print("Microsoft")   


zaki = Employee() 
zaki.language="Javascript"
zaki.greet()
zaki.company()
zaki.getinfo()
