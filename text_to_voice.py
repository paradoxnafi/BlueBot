import os

def textToVoice(text):
	#System will speak the string in text
	os.system('echo "%s" | festival --tts' %(text))
	
#textToVoice()