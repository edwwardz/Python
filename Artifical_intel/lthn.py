import speech_recognition as sr

engine = sr.Recognizer()
mic = sr.Microphone()
hasil = ""

with mic as source:
	print("Please Talk")
	rekaman = engine.listen(source)
	print("Time Out")

	try:
		hasil = engine.recognize_google(rekaman)
		print(hasil)
	except engine.UnknownValueError:
		print("Please Try again")
	except Exception as e:
		print(e)


