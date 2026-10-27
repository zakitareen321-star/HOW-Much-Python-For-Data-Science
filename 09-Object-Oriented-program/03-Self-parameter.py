class Employee:
    language="Python"   
    Salary="150000$"

    def getinfo(self):
        print(f"The language is {self.language}. and the Salary is {self.Salary}")

    def greet(self):
        print("Hello")


Egor = Employee()   
Egor.language="Javascript"
# print(Egor.language,Egor.Salary)
Egor.greet()
Egor.getinfo()