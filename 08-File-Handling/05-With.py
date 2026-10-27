f=open("file.txt","r") 
file = f.read()  
print(file)
f.close()

# The same thing  can also be done this way.
with open("file.txt","r")as f:
    print(f.read())              # we don't have explicitly close the file using "with" your  file is automatically close





# create a new page and then write in this page
str="“I am creating a repository on GitHub.”"
with open("page.txt","w") as f :
    f.write(str)