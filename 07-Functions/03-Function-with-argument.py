def GoodDay(name,ending):        #   name & ending is argument
    print("Good Day " + name)    #   Arguments make a function dynamic—it can work with different names..
    print(ending)
    

GoodDay ("Ali"," Thankx for watching")   
GoodDay("Sana", "Thankx for coming")
GoodDay("Egor", "Thankx for shopping")     # You don’t need to create a separate function for each name. Just create one function and pass each name to it.
GoodDay("Haya","Thanks for joining us")




# Return value
def GoodDay(name,starting):   
    print("Good day", name, )
    print(starting)
    return "Work is done"  ## return value

GoodDay("Anas", "How is it going bro")   
GoodDay("Currren", "What are you doing this weekend")

a=GoodDay("Rehan","how is it going without Friends")
print(a) ## return value

