from dotenv import load_dotenv
import os
import json
import requests
from bs4 import BeautifulSoup
 
load_dotenv()

#Lista de Animes ya notificados
anime_list = []

def obtener_animes():
    # Ejecutar GET-Request
    response = requests.get(os.environ.get("ANIME_URL"))

    # Analizar sintácticamente el archivo HTML de BeautifulSoup del texto fuente
    html = BeautifulSoup(response.text, 'html.parser')

    anime_titles = html.find_all('div', class_="animes")

    animes = []

    for anime in anime_titles:
        print(anime.h2.text + " cap " + anime.p.text)
        animes.append(anime.h2.text + " cap " + anime.p.text)

    return animes


def mandar_notificación_telegram(animes):
    url = f"https://api.telegram.org/bot{os.environ.get('TELEGRAM_TOKEN')}/getUpdates"
    message = "hello from your telegram bot"
    url = f"https://api.telegram.org/bot{os.environ.get('TELEGRAM_TOKEN')}/sendMessage?chat_id={os.environ.get('CHAT_ID')}&text={message}"
    print(json.dumps(requests.get(url).json(), indent=4))


if __name__ == '__main__':
    animes = obtener_animes()