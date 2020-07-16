import speech_recognition as sr
import os
import sys
import re
import webbrowser
import smtplib
import requests
import subprocess
from pyowm import OWM
#import youtube_dl
#import vlc
import urllib
import urllib3
import json
#from bs4 import BeautifulSoup as soup
#from urllib3 import urlopen
#import wikipedia
#import random
from time import strftime
import win32com.client as wincl



def myCommand():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print('Say something...')
		r.pause_threshold = 1
		r.adjust_for_ambient_noise(source, duration=1)
		audio = r.listen(source)
	try:
		command = r.recognize_google(audio).lower()
		print('You said: ' + command + '\n')
	#loop back to continue to listen for commands if unrecognizable speech is received
	except sr.UnknownValueError:
		print('....')
		command = myCommand();
	return command


#text to speech...
def sofiaResponse(audio):
	print(audio)
	for line in audio.splitlines():
		speak = wincl.Dispatch("SAPI.SpVoice")
		speak.Speak(audio)

def assistant(command):
	if 'hello' in command:
		day_time = int(strftime('%H'))
		if day_time < 12:
			sofiaResponse('Hello Sir. Good morning')
		elif 12 <= day_time < 18:
			sofiaResponse('Hello Sir. Good afternoon')
		else:
			sofiaResponse('Hello Sir. Good evening')
	elif 'old town road' in command:
		sofiaResponse('''Yeah, I'm gonna take my horse to the old town road
I'm gonna ride 'til I can't no more
I'm gonna take my horse to the old town road
I'm gonna ride 'til I can't no more (Kio, Kio)
I got the horses in the back
Horse tack is attached
Hat is matte black
Got the boots that's black to match
Ridin' on a horse, ha
You can whip your Porsche
I been in the valley
You ain't been up off that porch, now
Can't nobody tell me nothin'
You can't tell me nothin'
Can't nobody tell me nothin'
You can't tell me nothin'
Ridin' on a tractor
Lean all in my bladder
Cheated on my baby
You can go and ask her
My life is a movie
Bull ridin' and boobies
Cowboy hat from Gucci
Wrangler on my booty
Can't nobody tell me nothin'
You can't tell me nothin'
Can't nobody tell me nothin'
You can't tell me nothin'
Yeah, I'm gonna take my horse to the old town road
I'm gonna ride 'til I can't no more
I'm gonna take my horse to the old town road
I'm gonna ride 'til I can't no more
I got the''')
	else:
		sofiaResponse('Wrong Command!!!')

while True:
	assistant(myCommand())




