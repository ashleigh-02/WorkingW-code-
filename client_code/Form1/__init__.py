from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    self.init_components(**properties)

  def button_1_click(self, **event_args):
    city = self.text_box_1.text.strip()

    if not city:
      alert("Please enter a city name.")
      return

    # Call the server function to get weather
    weather = anvil.server.call("get_weather", city)

    if weather['success']:
      # Open the WeatherForm and pass the city + weather data
      open_form('WeatherForm', city=city, weather=weather)
    else:
      alert(f"Error: {weather['message']}")
