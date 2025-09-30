import anvil.server

#import anvil.server
import requests

API_KEY = "6b906bc379c14c275ee6514efd09338e"

def suggest_clothing(temp, condition):
  if temp < 0:
    suggestion = "Heavy coat, gloves, scarf"
    self.label_icon.text = "HeavyCoat_.png, 🧤, 🧣"
  elif 0 <= temp <= 10:
    suggestion = "Jacket, sweater, long pants"
    self.label_icon.text = "Jacket_.png, Sweater_.png, 👖"
  elif 11 <= temp <= 15:
    suggestion = "Light jacket, long sleeve, long pants"
    self.label_icon.text = "LightJacket_.png, longsleeve_.png, 👖"
  elif 16 <= temp <= 20:
    suggestion = "Light jacket, short sleeve, long pants"
    self.label_icon.text = "LightJacket_.png,👚,👖"
  elif 21 <= temp <= 25:
    suggestion = "T-shirt, shorts, sunglasses"
    self.label_icon.text = "👚 🩳 🕶️"
  elif 26 <= temp <= 32:
    suggestion = "singlet, shorts, hat, sunglasses"
    self.label_icon.text = "Singlet.png, 🩳, 🕶️, 👒"
  else:
    suggestion = "Light clothing, hat, sunglasses"

  if condition.lower() in ['rain', 'snow']:
    suggestion += " + waterproof jacket or umbrella"
    self.label_icon.text = "Raincoat.png, 🌂"
  return suggestion

@anvil.server.callable
def get_weather(location):
  url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={API_KEY}"
  result = requests.get(url)

  if result.status_code == 200:
    data = result.json()
    temp = data['main']['temp']
    condition = data['weather'][0]['main']
    suggestion = suggest_clothing(temp, condition)
    return {"success": True, "temp": temp, "condition": condition, "suggestion": suggestion}
  else:
    return {"success": False, "message": result.json().get("message", "Unknown error")}