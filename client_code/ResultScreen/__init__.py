from ._anvil_designer import WeatherFormTemplate
from anvil import *
from anvil import open_form

class WeatherForm(WeatherFormTemplate):
  def __init__(self, city=None, weather=None, **properties):
    self.init_components(**properties)

    if city and weather:
      # Display info
      self.label_weather_info.text = f"🌦️ Weather in {city}: {weather['condition']} ({weather['temp']}°C)"
      self.label_suggestion.text = f"👕 Clothing Suggestion: {weather['suggestion']}"

  def button_back_click(self, **event_args):
    # Go back to the input form
    open_form('Form1')
