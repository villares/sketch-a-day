import requests
import tomllib

with open('/home/villares/api_tokens', 'rb') as f:
    api_tokens = tomllib.load(f)
    
API_KEY = api_tokens['openweathermap']['api_key']

# Set the latitude and longitude for the location you're interested in
latitude = '23.5475'
longitude = '-46.6361'

# URL for the OpenWeather Current Weather Data API
url = 'https://api.openweathermap.org/data/2.5/weather'
url_params = f'?lat={latitude}&lon={longitude}&units=metric&appid={API_KEY}'
# Make a request to the OpenWeather API
response = requests.get(url + url_params)

# Check if the request was successful
if response.status_code == 200:
    # Convert the response to JSON
    data = response.json()
    
    # Extract and print the temperature, weather description, and more
    temperature = data['main']['temp']
    weather_description = data['weather'][0]['description']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    
    print(f'Temperature: {temperature} C')  # &units=metric for C imperial for F
    print(f'Weather Description: {weather_description}')
    print(f'Humidity: {humidity}%')
    print(f'Wind Speed: {wind_speed} meter/sec')
else:
    print(response.status_code, 'Failed to retrieve data')