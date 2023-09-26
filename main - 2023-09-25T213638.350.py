import requests
import time

# Replace with your weather API endpoint and API key
WEATHER_API_ENDPOINT = "https://api.weatherapp.com/weather"
WEATHER_API_KEY = "your_weather_api_key"

# Replace with your sprinkler timer API endpoint and credentials
SPRINKLER_API_ENDPOINT = "https://api.sprinklertimer.com/control"
SPRINKLER_USERNAME = "your_username"
SPRINKLER_PASSWORD = "your_password"

def get_weather_data():
    try:
        params = {"api_key": WEATHER_API_KEY}
        response = requests.get(WEATHER_API_ENDPOINT, params=params)
        data = response.json()
        return data
    except Exception as e:
        print("Error fetching weather data:", e)
        return None

def stop_sprinkler():
    try:
        # Replace with the API call to stop the sprinkler timer
        # You may need to provide credentials or an API key
        payload = {
            "username": SPRINKLER_USERNAME,
            "password": SPRINKLER_PASSWORD,
            "action": "stop"
        }
        response = requests.post(SPRINKLER_API_ENDPOINT, data=payload)
        if response.status_code == 200:
            print("Sprinkler stopped.")
        else:
            print("Failed to stop sprinkler:", response.text)
    except Exception as e:
        print("Error stopping sprinkler:", e)

def main():
    while True:
        weather_data = get_weather_data()
        if weather_data:
            # Check if it's currently raining (replace with your actual weather data parsing)
            is_raining = weather_data.get("rain_status", False)
            if is_raining:
                stop_sprinkler()
            else:
                print("It's not raining. Sprinkler is running.")
        
        # Sleep for a while before checking again (adjust the interval as needed)
        time.sleep(3600)  # Sleep for 1 hour

if __name__ == "__main__":
    main()

