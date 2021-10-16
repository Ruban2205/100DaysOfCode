# Import Required for speech conversion
from gtts import gTTS
import os 

print("\nPython Text to speech Simulator\n")

# Getting input text from user. 
userInput = input("Enter the text: ")

# Setting language
language = "en"

# Passing text to the Engine. 
obj = gTTS(text=userInput, lang=language, slow=False)

askUser = input("\nDid you want to save the file? (y/n): ")
if askUser == "y":
    fileName = input("Enter the file name to save: ")
    obj.save(fileName + ".mp3")
    print(fileName, " Saved Successfully!!")
    
    play = input("Did you want to play the file?(y/n): ")
    if play == "y" or play == "Y":
        os.system(fileName + ".mp3")

    else:
        print("Okay!!")

else: 
    print("Your file was not Saved!!")