import speech_recognition as sr

engine = sr.Recognizer()
mic = sr.Microphone()
hasil = ""

with mic as source:
    print("Please Talk")
    rekaman = engine.listen(source)
    print("Okay please wait")

    try:
        hasil = engine.recognize_google(rekaman)
        print("You said: ", hasil)
    except engine.UnknownValueError:
        print("Please try again, something error")
    except Exception as e:
        print(e)