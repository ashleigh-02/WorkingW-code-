import anvil.server
import requests

API_KEY = "6b906bc379c14c275ee6514efd09338e"

def suggest_clothing(temp, condition):
  """Return clothing suggestion and emoji string"""
  if temp < 0:
    suggestion = "Heavy coat, gloves, scarf"
    emoji = "🧥🧤🧣"
  elif 0 <= temp <= 10:
    suggestion = "Jacket, sweater, long pants"
    emoji = "🧥🧶👖"
  elif 11 <= temp <= 15:
    suggestion = "Light jacket, long sleeve, long pants"
    emoji = "🧥👕👖"
  elif 16 <= temp <= 20:
    suggestion = "Light jacket, short sleeve, long pants"
    emoji = "🧥👚👖"
  elif 21 <= temp <= 25:
    suggestion = "T-shirt, shorts, sunglasses"
    emoji = "👕🩳🕶️"
  elif 26 <= temp <= 32:
    suggestion = "Singlet, shorts, hat, sunglasses"
    emoji = "🩳👒🕶️"
  else:
    suggestion = "Light clothing, hat, sunglasses"
    emoji = "👒🕶️"

  # Weather-specific adjustments
  if condition.lower() in ['rain', 'snow']:
    suggestion += " + waterproof jacket or umbrella"
    emoji = "🌂🧥"

  return suggestion, emoji


@anvil.server.callable
def get_weather(location):
  """Fetch weather data and return temperature, condition, and clothing info"""
  url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={API_KEY}"
  result = requests.get(url)

  if result.status_code == 200:
    data = result.json()
    temp = data['main']['temp']
    condition = data['weather'][0]['main']
    suggestion, emoji = suggest_clothing(temp, condition)

    return {
      "success": True,
      "temp": temp,
      "condition": condition,
      "suggestion": suggestion,
      "emoji": emoji
    }

  else:
    return {
      "success": False,
      "message": result.json().get("message", "Unknown error")
    }
