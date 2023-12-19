# scripts/weather_functions.py

import requests
from PIL import Image, ImageDraw, ImageFont
import os
from datetime import datetime
from io import BytesIO
from dotenv import load_dotenv

load_dotenv()

# Funciones relacionadas con el clima

# Función que crea los datos del tiempo
def get_weather_data(city):
    api_key = os.getenv("API_KEY")
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(api_url)
    data = response.json()

    temp = int(data['main']['temp'] - 273.15)
    temp_feel = int(data['main']['feels_like'] - 273.15)
    min_temp = int(data['main']['temp_min'] - 273.15)
    max_temp = int(data['main']['temp_max'] - 273.15)

    return {
        "city": city,
        "condition": data['weather'][0]['main'],
        "temp": temp,
        "temp_feel": temp_feel,
        "min_temp": min_temp,
        "max_temp": max_temp
    }

def create_weather_image(city):
    api_key = os.getenv("API_KEY")
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    
    json_data = requests.get(api_url).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    temp_feel = int(json_data['main']['feels_like'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)

    # Create an image with white background
    image = Image.new('RGB', (357, 178), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", size=15)

    draw.text((10, 10), str(city), fill=(0, 0, 0), font=font, size=40)
    imageDirectory = os.path.join("images")
    try:
        icon = Image.open(os.path.join(imageDirectory, f"{condition}.png"))
    except:
        print("Image not found")
        icon = Image.new('RGB', (50, 50), (255, 255, 255))
    
    image_condition = icon.resize((50, 50))
    image.paste(image_condition, (10, 50))

    # Set the position for text
    # draw.text((70, 10), weather_data['condition'], fill=(0, 0, 0), font=font)
    draw.text((70, 30), f"Temp: {temp}°C", fill=(0, 0, 0), font=font)
    draw.text((70, 50), f"Feels like: {temp_feel}°C", fill=(0, 0, 0), font=font)
    draw.text((70, 70), f"Min: {min_temp}°C", fill=(0, 0, 0), font=font)
    draw.text((70, 90), f"Max: {max_temp}°C", fill=(0, 0, 0), font=font)
    
    # Image name = weather_image_<city>.png
    imageName = f"./export/weather_image_{city}.png"
    image.save(imageName)
    print("Weather image saved successfully.")

    return imageName

# Más funciones relacionadas con el clima si las tienes

