# Takes the Question as input(text) and returns answer as text

import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import json
import numpy
import pickle
import random
import tflearn
import tensorflow
import voice_to_text

with open("intents.json") as file:
	data = json.load(file)

with open("data.pickle", "rb") as f:
	words, labels, training, output = pickle.load(f)

tensorflow.reset_default_graph()
# Nural network
net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)
model.load("model.tflearn")

def bagOfWords(s, words):
	bag = [0 for _ in range(len(words))]

	s_words = nltk.word_tokenize(s)
	s_words = [stemmer.stem(word.lower()) for word in s_words]

	for se in s_words:
		for i, w in enumerate(words):
			if w == se:
				bag[i] = 1

	return numpy.array(bag)


def genAnswer():
	print("=> Bot is listening: ")
	while True:
		Question = voice_to_text.speechToText()
		
		results = model.predict([bagOfWords(Question, words)])[0]
		results_index = numpy.argmax(results)
		tag = labels[results_index]

		if results[results_index] > 0.7:
			for tg in data["intents"]:
				if tg["tag"] == tag:
					responses = tg['responses']
			Answers = random.choice(responses)
			return Answers
		else:
			Answers = "Sorry. I am not sure what you mean."
			return Answers