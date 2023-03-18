from gtts import gTTS
import os 
from clase1 import *

text = summary
language = 'es'
speech = gTTS(text = text, lang = language, slow = False)
speech.save("voz.mp3")
os.system("start voz.mp3")


