import os
import voice_to_text

text = voice_to_text.speechToText()

def textToVoice():
	os.system(f'echo "{text}" | festival --tts')
	