import pyttsx3

engine = pyttsx3.init('sapi5')   # 🔴 FORCE Windows voice engine
engine.setProperty('rate', 160)
engine.setProperty('volume', 1.0)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # try 1 if 0 is silent

def speak(text):
    engine.say(text)
    engine.runAndWait()
