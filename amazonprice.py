from bs4 import BeautifulSoup
import requests
from datetime import datetime

# https://amzn.to/3E7V45Y -> Cetus Pro FPV

def cetus_price():
    r = requests.get('https://amzn.to/3E7V45Y')
    soup = BeautifulSoup(r.text, 'lxml')

    # price = span class="a-price-whole"
    price = soup.find_all('span', class_='a-price-whole')
    price_text = price[0].text

    output = ("The current price of Cetus Pro FPV is: " + price_text)
    print("Price Response send! and it is" + output)
    return output


# This only for developer support
def main():
    cetus_price()

if __name__ == "__main__":
    main()
