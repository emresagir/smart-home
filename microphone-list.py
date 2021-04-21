import speech_recognition as sr
miclist = sr.Microphone.list_microphone_names()
i = 0
for mic in miclist:
    
    print(str(i) +"-"+ mic)
    print("--------")
    i = i + 1
