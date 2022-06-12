from tkinter import *
import pyttsx3
import speech_recognition as sr

#text to speech conversion
def speak_text(text):
    friend=pyttsx3.init()
    friend.setProperty('rate', 200) 
    friend.setProperty('volume', 300) #remember to get this from gui values
    friend.say(text)
    friend.runAndWait()

#speech to text conversion
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # print('Listening...')
        audio = r.listen(source, phrase_time_limit=10) # avoid forever trigger
    
    # print('Recognizing...')
    try:
        MyText = r.recognize_google(audio)
        MyText = MyText.lower()
        rec_status = "Status: Processing.."
        # print("User Said: " + MyText)"
        return MyText

    except:
        return ""