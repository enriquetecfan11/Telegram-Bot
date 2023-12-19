from bs4 import BeautifulSoup
import requests

def get_stock_price(url, company_name):
    """
    Fetches the stock price and pre-market percentage of a company from Yahoo Finance.
    """
    headers = {'User-Agent': 'Mozilla/5.0'}  # Add a User-Agent header
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            price_element = soup.find("fin-streamer", class_="Fw(b) Fz(36px) Mb(-4px) D(ib)")

            # Fetch pre-market data
            pre_market_element = soup.find("span", class_=["C($positiveColor)", "C($negativeColor)"])
            pre_market_text = f", Pre-Market Change: {pre_market_element.text}" if pre_market_element else ", Pre-Market Data Not Available"

            if price_element:
                return f"{company_name} Precio hoy: ${price_element.text}{pre_market_text}"
            else:
                return f"Error: Stock price for {company_name} not found."
        else:
            return f"Error: Unable to access {url} (Status Code: {response.status_code})"
    except requests.exceptions.RequestException as e:
        return f"Error: Network-related error occurred - {e}"
    except Exception as e:
        return f"Error: An exception occurred - {str(e)}"

def allPrice():
    # Apple, Tesla, Facebook, Microsoft, Google, Amazon, Netflix, Nvidia
    companies = [
        ("https://finance.yahoo.com/quote/AAPL/", "Apple Inc. (AAPL)"),
        ("https://finance.yahoo.com/quote/TSLA/", "Tesla Inc. (TSLA)"),
        ("https://finance.yahoo.com/quote/META/", "Meta Platforms Inc. (FB)"),
        ("https://finance.yahoo.com/quote/MSFT/", "Microsoft Corporation (MSFT)"),
        ("https://finance.yahoo.com/quote/GOOG/", "Alphabet Inc. (GOOG)"),
        ("https://finance.yahoo.com/quote/AMZN/", "Amazon.com Inc. (AMZN)"),
        ("https://finance.yahoo.com/quote/NFLX/", "Netflix Inc. (NFLX)"),
        ("https://finance.yahoo.com/quote/NVDA/", "NVIDIA Corporation (NVDA)")

        # Add other companies as needed
    ]
    return "\n".join([get_stock_price(url, name) for url, name in companies])

if __name__ == '__main__':
    print(allPrice())
