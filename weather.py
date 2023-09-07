import requests
import os
from dotenv import load_dotenv
from datetime import timedelta, datetime

def get_weather(city):
    # Retrieving API key for OpenWeather app
    load_dotenv(dotenv_path=".env")
    api_key = os.getenv("API_KEY")

    url = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={api_key}'

    response = requests.get(url)
    if response.status_code != 200:
        print(response.status_code)
        return None

    data = response.json()
    latitude = data[0]["lat"]
    longitude = data[0]["lon"]

    print(latitude, longitude)

    url = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}'

    print(url)
    response = requests.get(url)
    if response.status_code != 200:
        return None
        
    weather_data = response.json()
    parsed_weather_data = parse_json(weather_data)
    print(parsed_weather_data)

    return weather_data

def KtoC(temp):
    return temp - 273.15

def KtoF(temp):
    return (temp - 273.15) * (9/5) + 32

def parse_json(data):
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    temp_min = data["main"]["temp_min"]
    temp_max = data["main"]["temp_max"]
    humidity = data["main"]["humidity"]
    descr = data["weather"][0]["description"]
    sunrise = data["sys"]["sunrise"]
    sunset = data["sys"]["sunset"]

    return {
        'temperature': "{:.2f}".format(KtoF(temp)) + "°F",
        'feels_like': "{:.2f}".format(KtoF(feels_like)) + "°F",
        'temp_min': "{:.2f}".format(KtoF(temp_min)) + "°F",
        'temp_max': "{:.2f}".format(KtoF(temp_max)) + "°F",
        'humidity': f"{humidity}%",
        'description': descr,
        'sunrise': "{} AM".format(datetime.fromtimestamp(sunrise)),
        'sunset': "{} PM".format(datetime.fromtimestamp(sunset)),
        'city': data["name"]
    }

def secondsToDate(s):
    return timedelta(seconds=s)

def main():
    get_weather()

if __name__ == "__main__":
    main()