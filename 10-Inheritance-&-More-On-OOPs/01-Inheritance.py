class folks:                   # Base class or Parent Class 
    Company= " Amazon"
    Work = " Data Scientist"
    Language= "Python"

    def info(self):
        print(f" We are working at {self.Company}  as  {self.Work}  with a strong command of {self.Language} ")

    @staticmethod
    def Show():
        print( " This is an Amaaing Oppertunity for those Student who are truely passioante about it") 

class Accept(folks):        # Derived class or Child Class
    pass

a=folks()    
b=Accept()              
b.info()
b.Show()
