from flask import Flask, render_template, request, url_for
from weather import get_weather, parse_json

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

@app.route('/weather')
def weather():

    city = request.args.get("city")

    weather_data = get_weather(city)

    if not weather_data:
        return "Failed to get weather data"

    # return weather_data
    return render_template('index.html', weather_data=parse_json(weather_data))