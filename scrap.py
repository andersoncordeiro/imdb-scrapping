import requests
import pandas as pd
from bs4 import BeautifulSoup


DICT_HEADER = {
  'User-Agent':
  'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36'
}


def get_soup(URL):
  response = requests.get(URL, headers=DICT_HEADER).content
  soup = BeautifulSoup(response, 'html.parser')
  return soup


def get_movies(genre):
  URL = 'https://www.imdb.com/calendar/?ref_=nv_mv_cal'
  soup = get_soup(URL)
  lista_lis = soup.find_all('li', class_='ipc-metadata-list-summary-item')
  for li in lista_lis:
    link = li.find('a')
    url = 'https://www.imdb.com' + link['href']
    list_genres = []
    try:
      generos = li.find_all('ul')[0]
      for genero in generos:
        list_genres.append(genero.text)
    except:
      pass
    if genre in list_genres:
      print(list_genres)
      print(link.text)
      print(url)
      print('-------------------------------\n')
      
      
get_movies('Drama')