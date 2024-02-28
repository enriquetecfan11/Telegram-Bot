import requests
from datetime import datetime
import logging


# Función para el comando /miestacion, que muestra el estado de una mi propia estación de temperatura
def miestacion():
  # Obtener los datos de la estación
  response = requests.get("http://192.168.1.77:5000/api/miniestacion")

  # Convertir los datos a formato JSON
  data = response.json()
  # print("Datos de la estacion: ", data)

  # Get the last data from the station
  data = data[-1]

  # Get createdAt from the data and convert it to datetime
  date = datetime.strptime(data['createdAt'], '%Y-%m-%dT%H:%M:%S.%fZ')

  # Get from createdAt the hour example 2023-12-20T15:54:12.633Z i need 15:54:12
  createdAt = datetime.strptime(data['createdAt'], '%Y-%m-%dT%H:%M:%S.%fZ')
  hour = createdAt.strftime("%H:%M:%S")

  # Create a string with the data
  message = f"""
  Datos de la mi estación de temperatura:

  - Temperatura: {data['temperatura']} ºC
  - Humedad: {data['humedad']} %
  - Presión: {data['presion']} hPa
  - Luxes: {data['luxes']} lux
  - Señal Wifi: {data['wifiRsii']} %
  - Altitud: {data['altura']} m
  - Fecha: {date.strftime('%d/%m/%Y')}
  - Hora: {hour}
  """

  return message