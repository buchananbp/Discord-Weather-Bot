import requests
# from main import userCity

# city = userCity
apiKey = "a5a9853714cfa7f4e265b5be2a6205df"
url = "https://api.openweathermap.org/data/2.5/weather?q=" + "Vestavia Hills" + "&units=imperial&appid=" + apiKey

# url = BASE_URL + "addid=" + apiKey + "&q=" + TEST_CITY + "&units=imperial"

weatherData = requests.get(url).json()

# Method to call current temp
# Handles exception where no data is found
def getCurrTemp():
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

# Method to call Daily hi & low
# Handles exception where no data is found
def getTempMinMax():
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

# Method to call weather description
# Handles exception where no data is found
def getMainInfo():
    if 'weather' in weatherData and len(weatherData['weather']) > 0:
    # Accessing the first weather object in the array
        current_weather = weatherData['weather'][0]
        if 'description' in current_weather:
            # Accessing the 'description' property of the current weather
            description = current_weather['description']
            return description
        else:
            return "Description not found in weather data."
    else:
        return "Weather data not found in the response."

def getClouds():
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
    

def printAll():
    return weatherData

# print("Cloudiness: " + str(weatherData['clouds']['all']) + "%")
# Testing
# print(getCurrTemp())
# print(getMainInfo())
# print(getTempMinMax())
print(getClouds())