from bs4 import BeautifulSoup
import requests

def fetch_news(url, tag, class_name):
    """
    Fetches the first two news headlines from a given URL.
    
    :param url: URL of the news site.
    :param tag: HTML tag where the news headline is located.
    :param class_name: Class name of the HTML tag.
    :return: A string containing the first two headlines or an error message.
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            news = soup.find_all(tag, class_=class_name)
            # headlines = [item.text for item in news[:2]]  # Get first two headlines
            return " ".join(news[0].text.split())  # Get first headline (remove newlines)
        else:
            return f"Error: Unable to access {url}"
    except Exception as e:
        return f"Error: An exception occurred - {str(e)}"


def noticias_economicas_español():
    return fetch_news('https://www.elespanol.com/invertia/', 'h3', "head head--l")



if __name__ == '__main__':
    print(noticias_economicas_español()) 