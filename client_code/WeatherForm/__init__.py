from ._anvil_designer import WeatherFormTemplate
from anvil import *

class WeatherForm(WeatherFormTemplate):
  def __init__(self, city=None, weather=None, **properties):
    self.init_components(**properties)

    if city and weather:
      # Display location in the top label
      self.label_1.text = f"📍 Location: {city}"
      self.label_1.font_size =22
      self.label_1.bold = True
      self.label_1.text_align = "center"

      # Display the emoji separately
      self.label_emoji.text = weather.get('emoji', '') 
      self.label_emoji.font_size = 32
      self.label_emoji.text_align = "center"

      # Display the outfit suggestion text
      self.label_suggestion.text = weather.get('suggestion', '')
      self.label_suggestion.font_size = 14
      self.label_suggestion.text_align = "center"

      #Display the weather 
      self.label_weather_info.text = f"🌦️ Weather in {city}: {weather['temp']}°C ({weather['condition']})"
      
      
  def button_back_click(self, **event_args):
    # Go back to the input form
    open_form('Form1')