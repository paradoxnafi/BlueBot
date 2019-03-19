import speech_recognition as SR 
R = SR.Recognizer() 

def speechToText():
	#Source of voice is microphone
	with SR.Microphone() as source:
		#Adjusting background noise
		R.adjust_for_ambient_noise(source, duration=1)
		voice = R.listen(source)
		#'text' is English text after converting voice into text
		text = R.recognize_google(voice)
		return text