#!/usr/env python3

import voice_to_text
import text_to_voice as ttv

text = voice_to_text.speechToText()
if text.find('hello', 0) > -1:
	ttv.textToVoice('Hello, I am happy to meet you')
elif text.find('hi', 0) > -1:
	ttv.textToVoice('Hi, I am doing just fine')
elif text.find('what', 0) > -1:
	if text.find('name', 0) > -1:
		ttv.textToVoice('Currently I am called Blue Bot')
elif text.find('tell', 0) > -1:
	if text.find('joke', 0) > -1:
		ttv.textToVoice('Why don\'t you tell us a joke?')
elif text.find('like', 0) > -1:
	if text.find('talk', 0) > -1:
		if text.find('people', 0) > -1:
			ttv.textToVoice('Yes, I love to talk with people and learn new things.')