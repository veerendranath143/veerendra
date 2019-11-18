import speech_recognition as sr
import pyaudio as p
import webbrowser as wb
r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()
with sr.Microphone() as source:
    r1.adjust_for_ambient_noise(source,duration=1)
    
    print("serach chrome or youtube")
    print("speak now")
    audio = r3.listen(source)
if "chrome" in r2.recognize_google(audio):
    r2 = sr.Recognizer()
    url = "https://www.google.com"
    with sr.Microphone() as source:
        print("serch your query")
        audio = r2.listen(source)
        try:
            get = r2.recognize_google(audio)
            print(get)
            wb.get().open_new(url+get)
        except Exception:
            print("error")

