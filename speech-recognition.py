import speech_recognition as sr
import time, playsound, os, random
from gtts import gTTS
import datetime
r = sr.Recognizer()
sr.Microphone.list_microphone_names()
def record_audio(ask=False):
    with sr.Microphone() as source: # microphone as source
        if ask:
            print(ask)
        audio = r.listen(source)  # listen for the audio via source
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError: # error: recognizer does not understand
            print('I did not get that')
        except sr.RequestError:
            print('Sorry, the service is down') # error: recognizer is not connected
        print(f">> {voice_data.lower()}") # print what user said
        return voice_data.lower()
    

def friday_speak(audio_string):
    tts=gTTS(text= audio_string ,lang="en")
    date_string = datetime.datetime.now().strftime("%d%m%Y%H%M%S")
    filename="hello"+date_string+".mp3"
    tts.save(filename)
    playsound.playsound(filename)

while 1:
    voice_data = record_audio()
    if "hello" in voice_data:
        friday_speak("hello to you")
    if "exit" in voice_data:
        friday_speak("Goodby")
        exit()