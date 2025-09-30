from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    self.init_components(**properties)

  def button_1_click(self, **event_args):
    # 1️⃣ Get city from textbox
    city = self.text_box_1.text.strip()

    if not city:
      self.label_weather.text = "Please enter a city."
      self.label_suggestion.text = ""
      self.image_icon.source = None
      return

      # 2️⃣ Call server function to fetch weather + clothing suggestion
    weather = anvil.server.call("get_weather", city)

    # 3️⃣ Handle server errors
    if not weather['success']:
      self.label_weather.text = f"Error: {weather['message']}"
      self.label_suggestion.text = ""
      self.image_icon.source = None
      return

      # 4️⃣ Update UI
    self.label_weather.text = f"Weather in {city}: {weather['condition']}, {weather['temp']}°C"
    self.label_suggestion.text = weather['suggestion']
    self.image_icon.source = weather['image_file']
