import requests
import time
from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='template folder') ## TEMPLATE FOLDER

def get_weather(api_key, lat, lon):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    parameters = {
        "lat": lat,
        "lon": lon,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=parameters)
    data = response.json()
    if data["cod"] == 200:
        weather_data = {
            "time": time.strftime("%Y-%m-%d %H:%M:%S"),
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"]
        }
        return weather_data
    else:
        return None

openweathermap_api_key = '00' #API KEY HERE

@app.route('/', methods=['GET', 'POST'])
def weather():
    if request.method == 'POST':
        latitude = request.form['latitude']
        longitude = request.form['longitude']
        weather_data = get_weather(openweathermap_api_key, latitude, longitude)
        if weather_data:
            return render_template('weather.html', weather=weather_data)
        else:
            return "Failed to fetch weather data."
    else:
        return render_template('weather.html', weather=None) #html file name

@app.route('/weather')
def weather_by_coordinates():
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    weather_data = get_weather(openweathermap_api_key, latitude, longitude)
    return jsonify(weather_data)

if __name__ == '__main__':
    app.run(debug=True)