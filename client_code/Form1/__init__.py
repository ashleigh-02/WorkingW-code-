from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
from .WeatherForm import WeatherForm  # Import second form
from anvil import open_form

class Form1(Form1Template):
  def __init__(self, **properties):
    self.init_components(**properties)

  def button_1_click(self, **event_args):
    city = self.text_box_1.text.strip()

    if not city:
      alert("Please enter a city name.")
      return

    # Call the server function
    weather = anvil.server.call("get_weather", city)

    if weather['success']:
      # Open the results screen
      open_form('WeatherForm', city=city, weather=weather)
    else:
      alert(f"Error: {weather['message']}")
