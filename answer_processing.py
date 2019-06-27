# Takes the Question as input(text) and returns answer as text
import voice_to_text

def genAnswer():
	Question = voice_to_text.speechToText()
	Answers = ''

	if Question.find('hello', 0) > -1:
		Answers = 'Hello, I am happy to meet you'
	elif Question.find('hi', 0) > -1:
		Answers = 'Hi, I am doing just fine'
	elif Question.find('what', 0) > -1:
		if Question.find('name', 0) > -1:
			Answers = 'Currently I am called Blue Bot'
	elif Question.find('tell', 0) > -1:
		if teouxt.find('joke', 0) > -1:
			Answers = 'Why don\'t you tell us a joke?'

	return Answers