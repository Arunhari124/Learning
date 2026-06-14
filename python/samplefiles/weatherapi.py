import requests




def get_weather(latitude,longitude,base_url):
    "https://api.open-meteo.com/v1/forecast"
    f"?latitude={latitude}"
    f"&longitude={longitude}"
    f"&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
    weather = requests.get(base_url).json()

    print(f"Temperature in {city}:",
      weather["current"]["temperature_2m"], "°C")
    
    
base_url="https://api.open-meteo.com/v1/forecast"
city=input("CITY?:")
geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
geo_data = requests.get(geo_url).json()
latitude = geo_data["results"][0]["latitude"]
longitude = geo_data["results"][0]["longitude"]
get_weather(latitude,longitude,base_url)