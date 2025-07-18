import requests

def get_weather(city_name):
    API_KEY = 'f0f14b6171da493c6cf32533a0ef2b9a'
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        weather_description = data['weather'][0]['description'].title()
        temperature = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        pressure = data['main']['pressure']

        print(f"\n📍 Weather Report For {city_name.title()}:\n")
        print(f"🌤️  Weather Condition: {weather_description}")
        print(f"🌡️  Temperature: {temperature}°C")
        print(f"🤗  Feels Like: {feels_like}°C")
        print(f"💧  Humidity: {humidity}%")
        print(f"🌬️  Wind Speed: {wind_speed} m/s")
        print(f"📈  Pressure: {pressure} hPa\n")

    elif response.status_code == 404:
        print("\n❌ City not found. Please check the spelling and try again.\n")
    else:
        print("\n⚠️  Failed to retrieve weather data. Please try again later.\n")

# Run the app
city_name = input("Enter city name: ").strip()
get_weather(city_name)