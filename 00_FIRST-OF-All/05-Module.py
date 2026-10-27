# Module 1
import os
# select the directory that you want to list
path = "C:\\Users\\zakit\\OneDrive\\Desktop"

contents = os.listdir(path)
# use os module to list the directory content
for item in contents:
    print(item)


# # MODULE 2
import pyjokes  # External module need to install using pip
joke = pyjokes.get_joke()  # pyjokes module ,, Method
print(joke)

# # MODULE 3
import emoji
print(emoji.emojize("Python is fun :angry_face: :smile:"))

# # MODULE 4
from colorama import Fore, Style
print(Fore.GREEN + "Muhammad zakariya")
print(Style.RESET_ALL)

# MODULE 5
import pyttsx3
engine = pyttsx3.init()
engine.say("""Hello Mam My name is Muhammad zakariya Khan Tareen
I am a Data scientist and a python Developer """)
engine.runAndWait()


# MODULE 6
import qrcode
img = qrcode.make("https://www.coursera.org")
img.save("myqr.png")
print(img)
