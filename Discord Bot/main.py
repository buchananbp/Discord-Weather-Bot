import discord
import requests
from discord.ext import commands

# # prefix for a command, i.e. listens for keyword to announce message

API_KEY = "a5a9853714cfa7f4e265b5be2a6205df"
TOKEN = "MTE1MzU0Mjg2MDAwNDY3MTU2MA.GaFajt.HowuLIbTZG4Oo911zhBnR4aC1QaUNu77YfaCSk"

intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", intents=intents)


# # # Prints a message to the terminal stating the bot is ready.
@client.event
async def on_ready():
    print("-------------------------------")
    print("\tThe Bot Is Ready!")
    print("-------------------------------")

# Receive user input for current town and store in variable currTown
@client.command()   
async def setup(ctx):
    await ctx.send("Hello, I am the Weather Pledge!")
    await ctx.send("I send out a location-based weather report every morning at 8am local time.")

    await ctx.send("Please call the \"!location\" command followed by the major city that you'd like to recieve weather data from.")

# This function gets the input from the user for a location they want the data from.
@client.command()
async def location(ctx, *city):
    # defines global vaiable userCity to be used in future weather data retrieval
    global userCity
    # Allows the user to enter in citys with two words. (i.e. New York)
    userCity = " ".join(city)
    await ctx.send("You entered: " + userCity + ".\n\nIf you'd like to change the city, please do that command again.")

# This is the command that gives the weather data, formatted in a string
@client.command()
async def weather(ctx):
    temp_min, temp_max = getTempMinMax()
    curr_temp = getCurrTemp()
    weather_description = getMainInfo()
    current_clouds = getClouds()
    weatherMessage = "Current Temperature: {}°F\nWeather Description: {}\nHigh: {}°F\nLow: {}°F \nCloudiness: {}%".format(
        curr_temp, weather_description, temp_max, temp_min, current_clouds)
    await ctx.send(weatherMessage)


def getCurrTemp():
    url = "https://api.openweathermap.org/data/2.5/weather?q=" + userCity + "&units=imperial&appid=" + API_KEY
    weatherData = requests.get(url).json()

    if 'main' in weatherData and len(weatherData['main']) > 0:
        currentTemp = weatherData['main']
        if 'temp' in currentTemp:
            currTemp = currentTemp['temp']
            return currTemp
            
        else:
            print("Current tempurature is not found in weather data.")
    else:
        print("Weather data not found in response.")
    return weatherData['main']['temp']

def getMainInfo():
    url = "https://api.openweathermap.org/data/2.5/weather?q=" + userCity + "&units=imperial&appid=" + API_KEY
    weatherData = requests.get(url).json()

    if 'weather' in weatherData and len(weatherData['weather']) > 0:
        current_weather = weatherData['weather'][0]
        if 'description' in current_weather:
            description = current_weather['description']
            return description
        else:
            return "Description not found in weather data."
    else:
        return "Weather data not found in the response."
    
def getTempMinMax():
    url = "https://api.openweathermap.org/data/2.5/weather?q=" + userCity + "&units=imperial&appid=" + API_KEY
    weatherData = requests.get(url).json()
    if 'main' in weatherData and len(weatherData['main']) > 0:
        min_max = weatherData['main']
        if 'temp_min' and 'temp_max' in min_max:
            temp_min = min_max['temp_min']
            temp_max = min_max['temp_max']
            return temp_min, temp_max
        else:
            print("Minimum and Maximum tempurature are not found in weather data.")
    else:
        print("Weather data not found in response.")

def getClouds():
    url = "https://api.openweathermap.org/data/2.5/weather?q=" + userCity + "&units=imperial&appid=" + API_KEY
    weatherData = requests.get(url).json()
    if 'clouds' in weatherData and len(weatherData['clouds']) > 0:
    # Accessing the first weather object in the array
        currentClouds = weatherData['clouds']
        if 'all' in currentClouds:
            # Accessing the 'description' property of the current weather
            clouds = currentClouds['all']
            return clouds
        else:
            return "Cloudiness not found in weather data."
    else:
        return "Weather data not found in the response."
    
client.run(TOKEN)
