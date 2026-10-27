import random

'''
1 for sanke
-1 for water
0 for gun
'''
computer= random.choice([-1, 0, 1])
youstr=input("Enter your choice:")
youDict={"s":1,"w":-1,"g":0}
reverseDict={1:"snake", -1:"Water", 0:"Gun"}         

you = youDict[youstr]                                 

# by now we have two numbers (variables), you and computer

print(f"you chose {(reverseDict[you])} \n  Computer chose {(reverseDict[computer])}")


if (computer== you):
    print("it's a draw")

else:                                          
    if (computer ==-1 and you == 1):
        print("yor win")

    elif(computer == -1 and you == 0):
        print("you lose")

    elif(computer == 1 and you == -1):        
        print("you lose")   

    elif(computer == 1 and you == 0):
        print("you win")

    elif(computer == 0 and you == 1):
        print("you lose")

    elif(computer == 0 and you == -1):
        print("you win") 

    else:
        print("Some thing went wrong")    




## The below logic is written on the basis of the value of computer - you   # THIS is SHORT BUT NOT READABLE .
## Comment out lines 23 to 43, then uncomment this one.
            
# else:
#     if ((computer-you)== -1 or (computer-you)== 2):    
#      print("you lose")
#     else:
#      print("you win")

