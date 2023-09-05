from flask import Flask, request, jsonify
from weather import get_weather
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/other')
def other():
    return "This is the other page..."

@app.route('/playing/<city>')
def playing(city):
    if not city:
        return "No city"
    return city

@app.route('/playing/')
def playingish():
    return "Forgot to give a city :P"

@app.route('/weather/<city>')
def weather(city):

    weather_data = get_weather(city)

    if not weather_data:
        return "Failed to get weather data"

    return weather_data