# Basic Weather App using Flask

## [www.guthib.com] Video (Coming Soon)

## Description

## Usage

Before you can use this app, you must first create an account with [https://openweathermap.org/] and get an API key. Input this API key into a .env file inside the directory in the format

```
API_KEY = "<API key goes here>"
```

### Windows (Does not currently)

Go to the command line and run the command 

```
pip install Flask
```

Then navigatre to the directory containing the app.py file and run with

```
python -m flask run
```

Then navigate to the port where the app is being exposed and tada!

### Mac

To run this on Mac, you'll first need to install flask [https://phoenixnap.com/kb/install-flask]


Install virtualenv
```
sudo python3 -m pip install virtualenv
```

cd into directory containing this project and run command
```
python3 -m venv weather-app
```

Activate environment
```
. weather-app/bin/activate
```

Install flask (if you do not already have it)
```
pip install Flask
```

cd into weather-app
```
cd weather-app
```

Set the flask app environment variable
```
export FLASK_APP=app.py
```

Run application
```
flask run
```

navigate to [http://127.0.0.1:5000/weather]
