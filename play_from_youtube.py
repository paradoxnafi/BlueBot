# This code is not in use with BlueBot.
# This code plays music from youtube.
# It takes a query and serch it on youtube.
# Then plays the first result.
# It downloads the video in mp3 format using youtube-dl 
import os
import urllib.request
from bs4 import BeautifulSoup
link = ''

print("Welcome, music bot at your service")
print("To exit, type /exit and hit enter")

while True:

	# Delets all mp3 files from current directory
	os.system('rm *.mp3')

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

    # This system command makes this code Linux only
    # Downloads specied song, plays it and then delets all mp3 from current directory
	command = 'youtube-dl -x --audio-format mp3 ' + link + ' && mpg123 *.mp3'
	os.system(command)