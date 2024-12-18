from django.shortcuts import render
from django.conf import settings
from .models import WeatherData
import requests

def get_weather(request):
    # Retrieve the API key from settings
    api_key = settings.WEATHER_API_KEY
    
    # Get city name from GET request parameter, default to 'Kochi' if not provided
    city = request.GET.get("city", "Kochi")
    
    # Construct the URL to fetch weather data from OpenWeather API
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        # Make the request to the OpenWeather API
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        
        # Parse the JSON response
        data = response.json()

        # Check if the response is successful
        if data.get("cod") == 200:
            # Extract relevant weather data from the response
            weather_data = {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"],
            }

            # Save the weather data in the database
            WeatherData.objects.create(**weather_data)
        else:
            # Handle error when the city is not found or there is an API issue
            weather_data = {"Error": "City not found or API issue occurred"}

    except requests.exceptions.RequestException as e:
        # Handle request exceptions
        weather_data = {"Error": str(e)}

    # Render the result to the 'index.html' template
    return render(request, "weather/index.html", {"data": weather_data})
