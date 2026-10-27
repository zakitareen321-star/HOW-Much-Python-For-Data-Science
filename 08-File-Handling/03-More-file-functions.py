# Readlines function
f=open("Readlines.txt")              
lines= f.readlines()         
                            
print(lines,type(lines))    
f.close()



# Readline function

f=open("Readlines.txt")
line1=f.readline()
print(line1,type(line1))


line2=f.readline()
print(line2,type(line2))

line3=f.readline()
print(line3,type(line3))

line4=f.readline()
print(line4,type(line4))

line5=f.readline()         # False
print(line5=="")

f.close()


# Doing same process using, while Loop


# f=open("Readlines.txt")
# line = f.readline()
# while(line != "" ):
#     print(line)
#     line = f.readline()

# f.close