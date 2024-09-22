import requests

def get_weather(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        
        # Parse the JSON response
        data = response.json()
        city = data["name"]
        country = data["sys"]["country"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather_description = data["weather"][0]["description"]

        print(f"Weather in {city}, {country}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Conditions: {weather_description.capitalize()}")
        
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")

def main():
    api_key = "30d4741c779ba94c470ca1f63045390a"
    
    location = input("Enter a city name or ZIP code: ")
    
    get_weather(api_key, location)

if __name__ == "__main__":
    main()
