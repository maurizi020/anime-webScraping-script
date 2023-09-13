from dotenv import load_dotenv
import os
import json
import requests
from bs4 import BeautifulSoup
 
load_dotenv()

if __name__ == '__main__':

    # Ejecutar GET-Request
    response = requests.get(os.environ.get("ANIME_URL"))

    # Analizar sintácticamente el archivo HTML de BeautifulSoup del texto fuente
    html = BeautifulSoup(response.text, 'html.parser')

    anime_titles = html.find_all('div', class_="animes")

    animes = []

    for anime in anime_titles:
        print(anime.h2.text + " cap " + anime.p.text)
    
    # print(json.dumps(animes, indent=4))