# WeatherApp

This is a simple weather application built using [Flet](https://flet.dev/) and [Flet Map](https://flet.dev/docs/controls/map). It allows users to enter a city name, fetch real-time weather data from the OpenWeatherMap API, and display the city's location on an interactive map.

## Features
- 🌡️ Fetch real-time weather data (temperature, humidity, weather description)
- 📍 Display city location on a map using OpenStreetMap tiles
- 🗪️ Move the map to the searched city's coordinates with smooth animation
- 📱 Mobile-friendly responsive UI

## Installation
### 1. Clone the Repository
```sh
git clone https://github.com/yourusername/weather-app-flet.git
cd weather-app-flet
```

### 2. Install Dependencies
Ensure you have Python installed, then install the required dependencies:
```sh
pip install flet flet-map requests
```

### 3. Obtain an API Key
- Sign up at [OpenWeatherMap](https://home.openweathermap.org/users/sign_up)
- Get your API key from [API Keys section](https://home.openweathermap.org/api_keys)
- Create a file `api_key.py` and add the following:
```python
API_KEY = "your_openweathermap_api_key"
```

## Usage
Run the application with:
```sh
python main.py
```
This will open the app in your browser.

## Project Structure
```
weather-app-flet/
├── main.py          # Main application file
├── api_key.py       # Contains OpenWeatherMap API key
├── requirements.txt # List of dependencies
├── README.md        # Project documentation
```

## Download App
You can download the APK from the following link:
[WeatherApp Download](https://www.mediafire.com/file/ifqmpgud6o8n4j6/WeatherApp.apk/file)

## License
This project is licensed under the MIT License.

