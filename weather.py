import requests
import os
from dotenv import load_dotenv
from datetime import timedelta
from flask import Flask, render_template

def get_weather():
    # Retrieving API key for OpenWeather app
    load_dotenv(dotenv_path=".env")
    api_key = os.getenv("API_KEY")

    city = input('Enter city name: ')

    url = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={api_key}'

    response = requests.get(url)
    if response.status_code != 200:
        print(response.status_code)
        return
        

    data = response.json()
    latitude = data[0]["lat"]
    longitude = data[0]["lon"]

    print(latitude, longitude)

    url = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}'

    print(url)
    response = requests.get(url)
    if response.status_code != 200:
        print(response.status_code, "2nd one")
        return
        
    weather_data = response.json()
    parsed_weather_data = parse_json(weather_data)
    print(parsed_weather_data)

def KtoC(temp):
    return temp - 273.15

def KtoF(temp):
    return (temp - 273.15) * (9/5) + 32

def parse_json(data):
    temp = data["main"]["temp"]
    feels_like = data["main"]["temp"]
    temp_min = data["main"]["temp"]
    temp_max = data["main"]["temp"]
    humidity = data["main"]["temp"]
    descr = data["weather"][0]["description"]
    sunrise = data["sys"]["sunrise"]
    sunset = data["sys"]["sunset"]
    return [
        str(KtoF(temp)) + "F", 
        str(KtoF(feels_like)) + "F", 
        str(KtoF(temp_min)) + "F", 
        str(KtoF(temp_max)) + "F", 
        humidity, descr, secondsToDate(sunrise), secondsToDate(sunset)]

def secondsToDate(s):
    return timedelta(seconds=s)

def main():
    get_weather()

if __name__ == "__main__":
    main()