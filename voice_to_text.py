# Listens to speech and returns it as text
import speech_recognition as sr 
r = sr.Recognizer() 

def speechToText():
	#Source of voice is microphone
	with sr.Microphone() as source:
		#Adjusting background noise
		r.adjust_for_ambient_noise(source, duration=1)
		try:
			voice = r.listen(source)
			Question = r.recognize_google(voice)
			return Question
		except Exception:
			# Recursively call this function if any issue or timeout
			speechToText()