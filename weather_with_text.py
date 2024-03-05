import requests
import time

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

def update_weather_file(weather_data):
    with open("file path", "a") as file:
        file.write(f"Date and Time: {weather_data['time']}\n")
        file.write(f"Temperature (ºC): {weather_data['temperature']}\n")
        file.write(f"Humidity (%): {weather_data['humidity']}\n")
        file.write(f"Description: {weather_data['description']}\n\n")

def main():
    openweathermap_api_key = '0000' #API KEY AQUI
    lat = input("Insert Lat: ")
    lon = input("Insert Long: ")

    while True:
        weather_data = get_weather(openweathermap_api_key, lat, lon)
        if weather_data is not None:
            print("Weather Data:")
            print("Date and Time:", weather_data["time"])
            print("Temperature (ºC):", weather_data["temperature"])
            print("Humidity (%):", weather_data["humidity"])
            print("Description:", weather_data["description"])

            # Update the weather data in the text file
            update_weather_file(weather_data)
        else:
            print("Error to obtain weather data.")
        
        time.sleep(1800)  

if __name__ == '__main__':
    main()