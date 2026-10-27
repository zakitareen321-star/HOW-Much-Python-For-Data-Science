def avg():  ## function definition
    a=int(input("Enter the number:"))
    b=int(input("Enter the number:"))   # return means the function gives back a value to wherever it was called, so it can be assigned to a variable.
    c=int(input("Enter the number:"))
    average=(a+b+c)/3
    print(average)

    return"The End"   ## value return concept


a =avg()
print(a)  #  return value

