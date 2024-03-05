import requests
import time
import tkinter as tk
from tkinter import messagebox

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

def get_weather_and_display():
    lat = lat_entry.get()
    lon = lon_entry.get()
    weather_data = get_weather(openweathermap_api_key, lat, lon)
    if weather_data is not None:
        result_text.set(f"Date and Time: {weather_data['time']}\nTemperature (ºC): {weather_data['temperature']}\nHumidity (%): {weather_data['humidity']}\nDescription: {weather_data['description']}")
    else:
        messagebox.showerror("Error", "Unable to obtain weather data.")

openweathermap_api_key = '00000' #API KEY HERE

# UI Setup
root = tk.Tk()
root.title("Weather App")

# Labels
lat_label = tk.Label(root, text="Latitude:")
lat_label.grid(row=0, column=0, padx=10, pady=5)
lon_label = tk.Label(root, text="Longitude:")
lon_label.grid(row=1, column=0, padx=10, pady=5)
result_label = tk.Label(root, text="Weather Result:")
result_label.grid(row=3, column=0, padx=10, pady=5)

# Entry Fields
lat_entry = tk.Entry(root)
lat_entry.grid(row=0, column=1, padx=10, pady=5)
lon_entry = tk.Entry(root)
lon_entry.grid(row=1, column=1, padx=10, pady=5)

# Result Text
result_text = tk.StringVar()
result_text.set("")
result_display = tk.Label(root, textvariable=result_text, wraplength=300, justify="left")
result_display.grid(row=3, column=1, padx=10, pady=5)

# Button
get_weather_button = tk.Button(root, text="Get Weather", command=get_weather_and_display)
get_weather_button.grid(row=2, columnspan=2, padx=10, pady=5)

root.mainloop()