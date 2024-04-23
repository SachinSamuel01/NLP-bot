import pyttsx3

def tts_response(text, voice):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for v in voices:
        print(v)
    if(voice == "Male"):
        engine.setProperty('voice', voices[0].id)
    elif(voice == "Female"):
        engine.setProperty('voice', voices[1].id)
    print("response: "+text)
    engine.say(text)
    engine.runAndWait()
