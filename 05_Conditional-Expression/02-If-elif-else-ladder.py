# if elif else, Collectively Called "ladder"


a= int(input("Enter your age:"))

if(a>=18):
    print("You are above the maximum age for this content.")
    print("You are now able to access this content.")

elif(a<0):
    print("You entered an invalid negative age. ")

elif(a==0):
    print("You entered 0, which is not a valid age.")    


else:
    print("You are below the minimum age for this content.")

print("end of program")    

