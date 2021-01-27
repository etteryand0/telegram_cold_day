import requests
from bs4 import BeautifulSoup

def parse() -> str:
    try:
        req = requests.get('http://ugms14.ru')
    except requests.exceptions.ConnectionError as e:
        return False, e

    html = BeautifulSoup(req.text, 'html.parser')

    content_block = html.find('div', class_='a2')
    meta = content_block.find('p', class_='mobfich')

    map_container = content_block.find('div', class_='map')
    weather_data = map_container.find('div', attrs={'class':'w39'})

    # parse meta
    meta = meta.text.split('.')[1].strip()


    # parse weather
    weather = list()

    weather_data = weather_data.text.strip().split('Температура:')
    weather.append(
        weather_data[0]
    )
    weather.append(
        weather_data[1].split('Давление:')[0].strip()
    )
    weather.append(
        weather_data[1].split('Ветер:')[1].strip()
    )


    return meta, weather
