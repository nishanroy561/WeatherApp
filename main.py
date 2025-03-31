import flet as ft
import flet_map as map
import requests
from api_key import API_KEY

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        lat = data["coord"]["lat"]
        lon = data["coord"]["lon"]
        return {
            "city": data["name"],
            "temp": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "weather": data["weather"][0]["description"],
            "lat": lat,
            "lon": lon,
        }
    return None

def main(page: ft.Page):
    page.title = "Weather App with Map"
    page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  # Center horizontally
    page.vertical_alignment = ft.MainAxisAlignment.CENTER  # Center vertically

    city_input = ft.TextField(label="Enter City", width=300)
    weather_text = ft.Text("", text_align=ft.TextAlign.CENTER)
    
    map_view = map.Map(
        width=350,  # Reduce width for mobile responsiveness
        height=300,  # Reduce height for better fit
        initial_center=map.MapLatitudeLongitude(20, 78),
        initial_zoom=5,
        layers=[
            map.TileLayer(url_template="https://tile.openstreetmap.org/{z}/{x}/{y}.png"),
            map.MarkerLayer(markers=[]),
        ],
    )

    def update_weather(e):
        city = city_input.value.strip()
        if city:
            weather_data = get_weather(city)
            if weather_data:
                weather_text.value = (
                    f"🌆 {weather_data['city']}\n"
                    f"🌡️ Temp: {weather_data['temp']}°C\n"
                    f"💧 Humidity: {weather_data['humidity']}%\n"
                    f"☁️ {weather_data['weather']}"
                )
                
                lat, lon = weather_data["lat"], weather_data["lon"]

                marker = map.Marker(
                    content=ft.Icon(ft.Icons.LOCATION_ON, color=ft.Colors.RED),
                    coordinates=map.MapLatitudeLongitude(lat, lon),
                )
                map_view.layers[1].markers.clear()
                map_view.layers[1].markers.append(marker)

                map_view.move_to(
                    destination=map.MapLatitudeLongitude(lat, lon),
                    zoom=12,  
                    animation_duration=500,
                )

                page.update()
            else:
                weather_text.value = "❌ City not found!"
                page.update()

    get_weather_btn = ft.ElevatedButton("Get Weather", on_click=update_weather)

    page.add(
        ft.Container(
            content=ft.Column(
                [
                    city_input, 
                    get_weather_btn, 
                    weather_text, 
                    map_view
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            alignment=ft.alignment.center,  # Centering in the page
            expand=True  # Makes sure the layout fills the screen
        )
    )

ft.app(main)
