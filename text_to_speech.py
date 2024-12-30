import pyttsx3

def speak_compliment(compliment):
    engine = pyttsx3.init()
    engine.say(compliment)
    engine.runAndWait()
