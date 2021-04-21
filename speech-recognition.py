import speech_recognition as sr
import time, playsound, os, random
from gtts import gTTS
import datetime
r = sr.Recognizer()

class Person:
    name = ''
    def setName(self, name):
        self.name = name

def is_exist(terms, string):
    for term in terms:
        if term in string:
            return True

def close_the_light():
    pass

def record_audio(ask=False):
    with sr.Microphone(device_index=1) as source: # microphone as source
        if ask:
            print(ask)
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)  # listen for the audio via source
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError: # error: recognizer does not understand
            friday_speak('I did not get that')
        except sr.RequestError:
            friday_speak('Sorry, the service is down') # error: recognizer is not connected
        print(f">> {voice_data.lower()}") # print what user said
        return voice_data.lower()
    

def friday_speak(audio_string):
    tts=gTTS(text= audio_string ,lang="en")
    date_string = datetime.datetime.now().strftime("%d%m%Y%H%M%S")
    filename="hello"+date_string+".mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def respond(string):
    if is_exist(["hi", "hello"], string):
        friday_speak("hello master, how can i help you")
    
    if is_exist(["how are you"], string):
        friday_speak("I feel wonderful, because you created me")
    
    if is_exist(["exit", "goodby"], string):
        friday_speak("Goodby")
        exit()
    
    if is_exist(["close the light", "close the lights", "turn off the light", "turn off the lights", "turn the lights off", "turn the light off", "turn off light", "turn off light"], string):
        friday_speak("Closing the lights")
        close_the_light()
    
    if is_exist(["what is your name", "what's your name"], string):
        if person_obj.name:
            friday_speak("my name is friday")
        else:
            friday_speak("my name is friday, what's your name")
    
    if is_exist(["my name is",], string):
        person_name = voice_data.split("is")[-1].strip()
        friday_speak("nice to meet you" + person_name)
        person_obj.setName(person_name)

    #else:
    #  friday_speak("I didn't get that")
    
person_obj = Person()
time.sleep(1)
while 1:
    voice_data = record_audio()
    respond(voice_data)
