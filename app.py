from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['get'])


def index():
    API_KEY = 'API_KEY'  
    city = request.args.get('q')  

    
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}'
    response = requests.get(url).json()

    
    if response.get('cod') != 200:
        message = response.get('message', '')
        weather = f'Error getting temperature for {city.title()}. Error message = {message}'
        return render_template('index.html', weather=weather)

    
    current_temperature = response.get('main', {}).get('temp')
    if current_temperature:
        current_temperature_celsius = round(current_temperature - 273.15, 2)
        weather =  f'Current temperature of {city} is {current_temperature_celsius} C '
        return render_template('index.html', weather=weather)
    else:
        weather = f'Error getting temperature for {city.title()}'
        return render_template('index.html', weather=weather)
    

if __name__=='__main__':
	app.run()
