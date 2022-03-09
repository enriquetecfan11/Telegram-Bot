from bs4 import BeautifulSoup 
import requests

def apple_price():
      main_url = "https://finance.yahoo.com/quote/AAPL/"
      req = requests.get(main_url)
      soup = BeautifulSoup(req.text, "html.parser")
      ApplePrice = soup.find("fin-streamer", class_ = "Fw(b) Fz(36px) Mb(-4px) D(ib)")
      output = "Apple Inc.(APPL) today: $" + ApplePrice.text
      return output

def tesla_price():
      main_url = "https://finance.yahoo.com/quote/TSLA"
      req = requests.get(main_url)
      soup = BeautifulSoup(req.text, "html.parser")
      ApplePrice = soup.find("fin-streamer", class_ = "Fw(b) Fz(36px) Mb(-4px) D(ib)")
      output = "Tesla Inc.(TSLA) today: $" + ApplePrice.text
      return output

def meta_price():
      main_url = "https://finance.yahoo.com/quote/FB"
      req = requests.get(main_url)
      soup = BeautifulSoup(req.text, "html.parser")
      MetaPrice = soup.find("fin-streamer", class_ = "Fw(b) Fz(36px) Mb(-4px) D(ib)")
      output = "Meta Platforms Inc.(FB) today: $" + MetaPrice.text
      return output


def micro_price():
      main_url = "https://finance.yahoo.com/quote/MSFT"
      req = requests.get(main_url)
      soup = BeautifulSoup(req.text, "html.parser")
      MicrosoftPrice = soup.find("fin-streamer", class_ = "Fw(b) Fz(36px) Mb(-4px) D(ib)")
      output = "Microsoft Corporation (MSFT) today: $" + MicrosoftPrice.text
      return output

def stonksPrice():
        output = apple_price() + "\n" + tesla_price() + "\n" + meta_price() + "\n" + micro_price()
        print("Stonks Prices Sended!!")
        return output
