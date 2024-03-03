import requests
import time

def get_weather(api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    lat = 0000 ## latitude here
    lon = 0000 ## longitude here
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


openweathermap_api_key = 'API KEY HERE!!!!!!'

def write_to_file(weather_data, filename, alert_message = None):
    with open(filename, "a") as file:
        file.write(f"Time: {weather_data['time']}\n")
        file.write(f"Temperature: {weather_data['temperature']}°C\n")
        file.write(f"Humidity: {weather_data['humidity']}%\n")
        file.write(f"Description: {weather_data['description']}\n\n")
        if alert_message:
            file.write(f"Alert: {alert_message}\n\n")
        else:
            file.write("\n")
        
filename = "ENTER YOUR FILEPATH HERE"
t_upper_threshold = 28 #ºC
t_lower_threshold = 10 #ºC

while True:
    weather_data = get_weather(openweathermap_api_key)
    if weather_data:
        if weather_data['temperature'] > t_upper_threshold:
            alert_message = ("The Temperature is too high, stay hidrated!")
        elif weather_data['temperature'] < t_lower_threshold:
            alert_message = ("The Temperature is too low, stay warm!")
        else:
            alert_message = None
    
        write_to_file(weather_data, filename)
        print("Weather data recorded.")
    else:
        print("Failed to fetch weather data.")
    
    time.sleep(1800)  # 30min interval