# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 23:28:32 2022

@author: brunsj2
"""

import ctypes, requests, json, random, time
from PIL import Image, ImageDraw, ImageFont

# Variables
    # Sizes
width = 3840
length = 2400
side_length = 2800
    # Colors
teal_blue = "#252f3b"
light_blue = (109, 125, 145)
file_name = "Absolute Path"
    # Fonts
myFont = ImageFont.truetype('Ubuntu-Italic.ttf', 100)
myFont2 = ImageFont.truetype('Ubuntu-Italic.ttf', 50)
    # Weather
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
CITY = "Albany"
API_KEY = "your api key for OpenWeather"
URL = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
temperature = "error"
humidity = "error"
report = "error"
    # Emotes
emotes = ["[¬º-°]¬", ":-)", ":)", "B-)", ':/', "=D", "=3", ":D"]

while True:
    random_emote = random.randint(0, len(emotes) - 1)
    emote = emotes[random_emote]
    
    # Open Weather API
    # HTTP request
    response = requests.get(URL)
    # getting data in the json format
    data = response.json()
    
    # checking the status code of the request
    
    if data["cod"] != 404:
       # getting the main dict block
       main = data['main']
       temperature = main['temp']
       temperature = ((temperature - 273.15) * (9 / 5)) + 32
       humidity = main['humidity']
       report = data['weather'][0]["description"]
       print(f"{CITY:-^30}")
       print(f"Temperature: {temperature}")
       print(f"Humidity: {humidity}")
       
    else:
       # showing the error message
       print("Error in the HTTP request")
    
    # Notes
    note = open(r"C:\Users\brunsj2\Dropbox\PC\Documents\Side Projects\BGChanger\Notes\To-Do List.txt")
    note_text = note.readline()
    if len(note_text) > 25:
        temp = note_text[0:26]
        temp += "..."
        note_text = temp
    note.close()
    
    # Image formatting
    img = Image.new("RGB", (width, length))
    rect = ImageDraw.Draw(img)
    rect.rectangle([(0,0), (width, length)], fill = teal_blue)
    rect.text((side_length, 1000), "weather", fill = light_blue, font = myFont)
    rect.text((side_length, 1150), "{:.1f}°\n{}".format(temperature, report), fill = light_blue, font = myFont2)
    rect.text((side_length, 1500), "notes", fill = light_blue, font = myFont)
    rect.text((side_length, 1650), note_text, fill = light_blue, font = myFont2)
    rect.text((side_length, 2000), "joshua brunscheen \n{}".format(emote), fill = light_blue, font = myFont)
    img.save(file_name)
    
    # Change wallpaper
    ctypes.windll.user32.SystemParametersInfoW(20, 0, file_name , 0)
    time.sleep(3)
