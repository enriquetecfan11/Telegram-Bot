import requests
from PIL import Image, ImageDraw, ImageFont
import os
from datetime import datetime
from io import BytesIO
from dotenv import load_dotenv
from bs4 import BeautifulSoup


# Function to scrape the Metro Madrid "La red en tiempo real" status
def scrape_metro_status():
    # URL of the Metro Madrid "La red en tiempo real"
    url = 'https://www.metromadrid.es/es'
    
    # Send a GET request to the URL
    response = requests.get(url)
    
    # If the response was successful, no Exception will be raised
    response.raise_for_status()
    
    # Initialize BeautifulSoup object to parse the content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Initialize a dictionary to store the status of each line
    line_statuses = {}
    
    # Loop through each line number
    for i in range(1, 12):
        # Construct the class name for the line image
        line_class = f'linea-{i}'

        print("Estado lineas del metro de Madrid")
        # Find the element with the specific class name
        line_element = soup.find(class_=line_class)
        
        # Check if the line element was found
        if line_element:
            # Find the status span related to the line using find_next to handle non-direct siblings
            status_element = line_element.find_next("span", class_=["state--green", "state--red"])
            
            # Check if the status element was found
            if status_element:
                # Determine the status based on the class of the status element
                if 'state--green' in status_element['class']:
                    status = 'Funcionamiento normal'
                elif 'state--red' in status_element['class']:
                    status = 'Servicio interrumpido'
                else:
                    status = 'No se ha podido determinar el estado'
            else:
                status = 'Status element not found'
        else:
            status = 'No se ha podido determinar el estado'
        
        # Add the status to the dictionary
        line_statuses[f'Line {i}'] = status
    
    # Return the dictionary containing the statuses
    return line_statuses
