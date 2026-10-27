class Employee:
    language="Python"   
    salary="150000$"

    def getinfo(self):
        print(f"The language is {self.language}. and the salary is {self.salary} .and The name is {self.name}")


zaki = Employee()   
zaki.language="Javascript"
zaki.name="Zakariya"

zaki.getinfo()      # Function call