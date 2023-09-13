from dotenv import load_dotenv
import os
import json
import requests
from bs4 import BeautifulSoup
import time
 
load_dotenv()

#Lista de Animes ya notificados
anime_list = []


def obtener_animes():

    """ Función encargada de recolectar datos de la pag de anime, datos puros del inicio
        de la siguiente manera [Anime cap NumeroCap] """

    # Ejecutar GET-Request
    response = requests.get(os.environ.get("ANIME_URL"))

    # Analizar sintácticamente el archivo HTML de BeautifulSoup del texto fuente
    html = BeautifulSoup(response.text, 'html.parser')

    anime_titles = html.find_all('div', class_="animes")

    animes = []

    for anime in anime_titles:
        animes.append(anime.h2.text + " cap " + anime.p.text)

    return animes

def filtrar_animes(animes):
    """Funcion para filtrar los animes que ya han sido notificados de los nuevos"""
    
    animes_nuevos = []

    for anime in animes:
        if anime not in anime_list:
            animes_nuevos.append(anime)
    return animes_nuevos



def mandar_notificacion_telegram(animes):

    """ Función encargada de mandar mensaje de notificación con una lista de los animes que se actualizaron al bot de telegram """

    message = """Mira Becerrin estos son los nuevos animes: \n"""
    for anime in animes:
        message += f"-{anime}\n"
    

    url = f"https://api.telegram.org/bot{os.environ.get('TELEGRAM_TOKEN')}/sendMessage?chat_id={os.environ.get('CHAT_ID')}&text={message}"
    print(json.dumps(requests.get(url).json(), indent=4))



if __name__ == '__main__':

    iterator = 0
    while iterator < 1000:
        animes = obtener_animes()
        animes_nuevos = filtrar_animes(animes)

        if len(animes_nuevos) > 0:
            mandar_notificacion_telegram(animes_nuevos)
            anime_list = animes
        
        time.sleep(300)
        iterator += 1