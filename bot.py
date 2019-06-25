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
	if teouxt.find('joke', 0) > -1:
		ttv.textToVoice('Why don\'t you tell us a joke?')

'''

Answers = [
	'Hello, I am happy to meet you',
	'Currently I am called Blue Bot',
	"I don't eat anything.",
	'I love green.',
]

Keywords = [
	['hi', 'hello', 'how are you',],
	['what is your name', 'what should I call you', 'who'],
	['what', 'eat', 'like to eat', 'love to eat'],
	['What', 'favourite', 'colour', 'love'],
]

Counter = []

for i in range(len(Keywords)):
	for j in range(len(Keywords[i])):
		if Keywords[i][j] in text:
			Counter[i] += 1
Max = max(Counter)
ttv.textToVoice(Answers[max])
'''