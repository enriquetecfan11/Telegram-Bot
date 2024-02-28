<h1 align="center">Tecfan's Telegram-Bot</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/enriquetecfan11/telegram-bot?color=56BEB8">

## Description / Descripción

Welcome to the developer page of Tecfan's Telegram-Bot.

I wan to make this because i want to learn python, and i want to know what is the best way to make a bot.

I have twitter @enriquetecfan, if you want to follow me or ask  me something about the bot.


Bienvenido a la página de desarrollo del Telegram-Bot de Tecfan.

Quiero hacer esto porque quiero aprender python, y quiero saber cual es la mejor manera de hacer un bot.

Tengo twitter @enriquetecfan, por si quieres seguirme o preguntarme algo sobre el bot.

## Comandos del bot / Bot Commands

The bot have this comands:
- /start: Starts the bot
- /price <crypto name> : Displays the price of a cryptocurrency
- /weather <city name> : Displays the weather of a city
- /metro: Displays the status of Madrid Metro lines
- /hour: Displays the current time
- /stonks: Displays stock prices
- /news: Displays economic news
- /bolsa: Displays stock market opening times
- /station: Displays my temperature station data
- /generate <text>: Generates an image with the text we pass it.

El bot tiene estos comandos:
- /start: Inicia el bot
- /price <nombre crypto>: Muestra el precio de una criptomoneda
- /weather <nombre ciudad> : Muestra el tiempo de una ciudad
- /metro: Muestra el estado de las líneas de Metro de Madrid
- /hora: Muestra la hora actual
- /stonks: Muestra los precios de las acciones
- /noticias: Muestra las noticias económicas
- /bolsa: Muestra los horarios de apertura de las bolsas
- /miestacion: Muestra los datos de mi estación de temperatura
- /generate <texto>: Genera una imagen con el texto que le pasemos

## Para poder usar el bot con docker / To use the bot with docker

Tienes que ejecutar este comando:
```cli
docker build -t telegram-bot .
```

Y después, este:
```cli
docker run -d --restart=always --name telegram-bot telegram-bot
```
Y ya está, ya tienes el bot funcionando.

You have to execute this command:
```cli
docker build -t telegram-bot .
```

And then, this:
```cli
docker run -d --restart=always --name telegram-bot telegram-bot
```
And that's it, you have the bot working.
