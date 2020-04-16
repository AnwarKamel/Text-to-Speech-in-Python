from gtts import gTTS
import os

text = "Hi Anwar How are you "
text2 = " أهلا أنور كيف حالك  "

language ='en'

speech = gTTS(text = text , lang = language , slow = False)
speech.save("text.mp3")

os.system("start text.mp3")

