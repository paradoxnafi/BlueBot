import os
import urllib.request
from bs4 import BeautifulSoup
link = ''

print("Welcome, music bot at your service")
print("To exit, type /exit and hit enter")

while True:
	textToSearch = input('Enter your query: ')
	if textToSearch == '/exit':
		print('Good bye!!!')
		break
	query = urllib.parse.quote(textToSearch)
	url = "https://www.youtube.com/results?search_query=" + query
	response = urllib.request.urlopen(url)
	html = response.read()
	soup = BeautifulSoup(html, 'html.parser')
	for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
	    link = ('https://www.youtube.com' + vid['href'])
	    break

	command = 'youtube-dl -x --audio-format mp3 ' + link + ' && mpg123 *.mp3 && rm *.mp3'
	os.system(command)


