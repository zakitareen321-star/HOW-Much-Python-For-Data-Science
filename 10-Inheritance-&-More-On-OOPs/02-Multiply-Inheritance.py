# Multiply Inheritance  2 parent ,1 Child

class folks:                   # Base class or Parent Class 1
    Company= " Amazon"
    Work = " Data Scientist"
    Language= "Python"

    def info(self):
        print(f"We are working at {self.Company}  as  {self.Work}  with a strong command of {self.Language} ")

    @staticmethod
    def Show():
        print( "  This is an Amaaing Oppertunity for those Student who are truely passioante about it") 



class Accept():                   # Parent 2 
    Totalpercent  = "5000","90% "
    def Unicorn(self):            
        print(f" The Toal Workers in Unicorn and there percentage is {self.Totalpercent}")



class Amount(folks,Accept):              # Child 1
    pass


a=folks()                    
b=Accept()
c=Amount()
c.info()
c.Show()
c.Unicorn()
