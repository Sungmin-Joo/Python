# -*- coding: utf-8 -*-
'''
import speech_recognition as sr

r = sr.Recognizer()
#harvard = sr.AudioFile('hello.wav')

with sr.Microphone() as source:
    #audio = r.record(source)
    audio = r.listen(source)
try:
    print("You said " + r.recognize_google(audio,language = 'ko_KO'))    # recognize speech using Google Speech Recognition
except LookupError:                            # speech is unintelligible
    print("Could not understand audio")
    
'''




import speech_recognition as sr
import hbcvt

r = sr.Recognizer()
harvard = sr.AudioFile('hello.wav')

with harvard as source:
    audio = r.record(source)
    
a = r.recognize_google(audio,language = 'ko_KO')
b=[hbcvt.h2b.text(i) for i in a.split()]

'''
import speech_recognition as sr

r = sr.Recognizer()
source
with sr.Microphone() as source:
    print("say something")
    audio = r.listen(source)
    print("Time OVER")

try:
    print("text : " +r.recognize_google(audio,language = 'ko_KO'))
except:
    print('noob')'
'''