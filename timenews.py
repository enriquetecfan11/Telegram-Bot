from bs4 import BeautifulSoup
import requests
from datetime import datetime


def mondejar_weather():
    r = requests.get('https://www.wunderground.com/weather/es/mond%C3%A9jar/')
    soup = BeautifulSoup(r.text, 'lxml')

    tiempo = soup.find_all('span', class_='wu-value wu-value-to')
    texto_tiempo = int(tiempo[0].text)
    celsius = (texto_tiempo - 32) * 5/9
    redondeo = round(celsius)

    condiciones = soup.find_all('div', class_='condition-icon')
    condiciones_texto = condiciones[0].text

    output = ("Mondejar have now " + str(redondeo) +"ºC and have " + condiciones_texto)
    print("Weather Response send!")
    return output


def noticias():
    r = requests.get('https://www.elespanol.com/')
    soup = BeautifulSoup(r.text, 'lxml')
    news = soup.find_all('h2', class_="art__title")

    newslist = []
    for new in news:
        newslist.append(new)

    first = newslist[0]
    second = newslist[1]

    respone = first.text + second.text
    #print("News Response send!")
    return respone


def noticias_economicas():
    r = requests.get('https://www.elespanol.com/invertia/')
    soup = BeautifulSoup(r.text, 'lxml')
    news = soup.find_all('h3', class_="head head--l")

    newslist = []
    for new in news:
        newslist.append(new)


    first = newslist[0]
    second = newslist[1]

    respuesta = first.text + second.text
    return respuesta
