# file imports
import speechrec

# lib imports
import os
from selenium import webdriver 
# from selenium.webdriver.common.by import by
import requests
import randfacts # get random facts
import random
from datetime import datetime

def search_web(text):
	driver = webdriver.Edge(executable_path="C:/Program Files (x86)/Microsoft\Edge/Application/msedge.exe")
	# driver.implicitly_wait(2)
	# driver.maximize_window()

	if 'youtube' in text.lower():
		speechrec.speak_text("Opening in youtube")
		indx = text.lower().split().index('youtube') # the word probably said before the query
		query = text.split()[indx + 1:] # the actual query and slicing input
		driver.get("http://www.youtube.com/results?search_query =" + '+'.join(query))
		driver.maximize_window()
		return

	elif 'wikipedia' in text.lower():

		speechrec.speak_text("Opening Wikipedia")
		indx = text.lower().split().index('wikipedia') 
		query = text.split()[indx + 1:]
		driver.get("https://en.wikipedia.org/wiki/" + '_'.join(query))
		return

	else:

		if 'google' in text:

			indx = text.lower().split().index('google')
			query = text.split()[indx + 1:]
			driver.get("https://www.google.com/search?q =" + '+'.join(query))

		elif 'search' in text:

			indx = text.lower().split().index('google')
			query = text.split()[indx + 1:]
			driver.get("https://www.google.com/search?q =" + '+'.join(query))

		else:

			driver.get("https://www.google.com/search?q =" + '+'.join(text.split()))

		return


# function used to open application present inside the system.
def open_application(text):
	try:
		os.startfile(text.lower()) # open program name as recognized by windows
		return
	except:
		speechrec.speak_text("Sorry, I could not find that application.")
		return

# function used to get weather using the OpenWeatherMap API
def get_weather(text):

	api_key = "44568c9f3587506a4c088c61a1cbbe7e" #personal weather API
	# base_url variable to store url
	base_url = "http://api.openweathermap.org/data/2.5/weather?"

	# Give city name
	indx = text.lower().split().index('in') #most likely word before city name
	city_words = text.split()[indx + 1:]
	city_name = ""
	city_name = city_name.join(city_words)
	print(city_name)
	complete_url = base_url + "appid=" + api_key + "&q=" + city_name
	print(complete_url)
	response = requests.get(complete_url)

	x = response.json()

	# Now x contains list of nested dictionaries
	# Check the value of "cod" key is equal to
	# "404", means city is found otherwise,
	# city is not found

	if x["cod"] != "404":
		y = x["main"]
		current_temperature = int(y["temp"]-273)
		current_humidity = y["humidity"]
		z = x["weather"]
		weather_description = z[0]["description"]
		#speak
		speechrec.speak_text("The temperature in celcius is " + str(current_temperature))
		speechrec.speak_text("and the humidity is " + str(current_humidity))
		speechrec.speak_text("The weather is " + str(weather_description))
		return

	else:
		speechrec.speak_text("Sorry, I could not find the weather for the city.")
		return

# Function to generate random numbers and get random facts
def get_random(text):
	if "facts" in text or "fact" in text:
		speechrec.speak_text("Did you know " + str(randfacts.get_fact(True)))
		return
	if "number" in text or "numbers" in text:
		speechrec.speak_text("The random number is " + str(random.randint()))
		return
	else:
		speechrec.speak_text("Sorry, I don't understand")
		return

def get_time():
	speechrec.speak_text(str(datetime.today().strftime("%I:%M %p")))

def get_date():
	speechrec.speak_text(str(datetime.today().strftime("%B %d %Y")))

def flip_coin():
	if random.randint(1,2) == 1:
		speechrec.speak_text("I Choose Heads")
	else:
		speechrec.speak_text("I Choose Tails")

