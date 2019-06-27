# Converts text into voice.
# Using 'Festival' voice engine on Linux.
import os
import answer_processing

def textToVoice():
	Answer = answer_processing.genAnswer()
	#System will speak the string in Answer
	os.system('echo "%s" | festival --tts' %(Answer))
	# Recursively calling this function to keep the program running
	textToVoice()