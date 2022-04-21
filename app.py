# Import the required module for text 
# to speech conversion
from gtts import gTTS
  
# This module is imported so that we can 
# play the converted audio
import os
  
# The text that you want to convert to audio
mytext1 = 'I love Bangladesh'
mytext2 = 'আমার   সোনার বাংলা, আমি তোমায় ভালোবাসি'
  
# Language in which you want to convert
language1 = 'en'
language2 = 'bn'
  
# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj1 = gTTS(text=mytext1, lang=language1, slow=False)
myobj2 = gTTS(text=mytext2, lang=language2, slow=False)
  
# Saving the converted audio in a mp3 file named
# welcome 
myobj1.save("1.mp3")
myobj2.save("2.mp3")
  
# # Playing the converted file
# os.system("mpg321 welcome.mp3")


