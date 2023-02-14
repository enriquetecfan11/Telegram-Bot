from bs4 import BeautifulSoup
import requests
from datetime import datetime

# https://amzn.to/3E7V45Y -> Cetus Pro FPV

def cetus_price():
  url = 'https://amzn.to/3E7V45Y'
  headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

  response = requests.get(url, headers=headers)
  soup = BeautifulSoup(response.content, 'html.parser')

  price = soup.find('span', attrs={'class': 'a-offscreen'}).text

  price_text = "The current price of Cetus Pro FPV is: " + str(price)

  return price_text
