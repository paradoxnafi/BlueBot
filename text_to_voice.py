import os
import voice_to_text

#Return value of speechToText() method from voice_to_text module is stored in text varibale
text = voice_to_text.speechToText()

def textToVoice():
	#System will speak the string in text
	os.system('echo "%s" | festival --tts' %(text)) 
	
