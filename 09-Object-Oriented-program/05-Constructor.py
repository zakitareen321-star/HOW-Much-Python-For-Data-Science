# dunder method are those method which starts from underscore

class Employee:
    language="Python"   
    salary="150000$"


    def __init__(self):                             # dunder mathod ,which is 'automatically call'
        print("This is for our kind and geneous Data Scientist Team")


    def __init__(self, name,language , salary): 
        self.name=name
        self.language=language
        self.salary=salary
        print("This is for our kind and geneous Data Scientist Team")


Aman = Employee("Aman khan","150000$","R")   
# Aman.name="Aman Khan"
print(Aman.name,Aman.salary,Aman.language)



Sajjad=Employee("Sajjad","1500000$","Javascript")
print(Sajjad.salary,Sajjad.language,Sajjad.name)