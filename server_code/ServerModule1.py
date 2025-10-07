import anvil.server
import requests

API_KEY = "6b906bc379c14c275ee6514efd09338e"

def suggest_clothing(temp, condition):
  # Suggest based on temperature
  if temp < 0:
    suggestion = "🧤 Heavy coat, gloves, scarf"
  elif 0 <= temp <= 10:
    suggestion = "🧥 Jacket, sweater, long pants"
  elif 11 <= temp <= 15:
    suggestion = "🧣 Light jacket, long sleeve, long pants"
  elif 16 <= temp <= 20:
    suggestion = "👕 Light jacket, short sleeve, long pants"
  elif 21 <= temp <= 25:
    suggestion = "👚 T-shirt, shorts, sunglasses 🕶️"
  elif 26 <= temp <= 32:
    suggestion = "👒 Singlet, shorts, hat, sunglasses"
  else:
    suggestion = "🩳 Light clothing, hat, sunglasses"

  # Add rain/snow condition
  if condition.lower() in ['rain', 'snow']:
    suggestion += " + waterproof jacket or umbrella 🌂"

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
import anvil.server
import requests

API_KEY = "6b906bc379c14c275ee6514efd09338e"

def suggest_clothing(temp, condition):
  # Suggest based on temperature
  if temp < 0:
    suggestion = "🧤 Heavy coat, gloves, scarf"
  elif 0 <= temp <= 10:
    suggestion = "🧥 Jacket, sweater, long pants"
  elif 11 <= temp <= 15:
    suggestion = "🧣 Light jacket, long sleeve, long pants"
  elif 16 <= temp <= 20:
    suggestion = "👕 Light jacket, short sleeve, long pants"
  elif 21 <= temp <= 25:
    suggestion = "👚 T-shirt, shorts, sunglasses 🕶️"
  elif 26 <= temp <= 32:
    suggestion = "👒 Singlet, shorts, hat, sunglasses"
  else:
    suggestion = "🩳 Light clothing, hat, sunglasses"

  # Add rain/snow condition
  if condition.lower() in ['rain', 'snow']:
    suggestion += " + waterproof jacket or umbrella 🌂"

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
