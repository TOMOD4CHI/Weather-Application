import requests
import time
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class WeatherApp(App):
    def build(self):
        return WeatherLayout()

    def get_weather(self):
        city_name = self.root.ids.city_input.text
        api_key = 'xxxx'
        base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'

        response = requests.get(base_url)
        data = response.json()

        if data['cod'] != '404':
            main = data['main']
            temperature = main['temp']
            pressure = main['pressure']
            humidity = main['humidity']
            weather_description = data['weather'][0]['description']
            sunrise_time=time.localtime(data['sys']['sunrise'])
            sunset_time=time.localtime(data['sys']['sunset'])

            weather_info = f'Temperature: {temperature}°C\n' \
                           f'Pressure: {pressure} hPa\n' \
                           f'Humidity: {humidity}%\n' \
                           f'Description: {weather_description}\n'\
                           f'Sunrise: {time.strftime("%H:%M", sunrise_time)}\n'\
                           f'Sunset: {time.strftime("%H:%M", sunset_time)} '
        else:
            weather_info = 'City Not Found'

        self.root.ids.weather_label.text = weather_info

class WeatherLayout(BoxLayout):
    pass

if __name__ == '__main__':
    WeatherApp().run()
