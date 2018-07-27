import time
import urllib
import requests
from bs4 import BeautifulSoup

movies = []


def get_movies(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    # parent node
    parent = soup.find(class_='grid_view')
    for movie in parent.find_all('li'):
        get_info(movie)


def get_info(movie):
    global movies
    name = movie.find(class_='title').string
    rate = movie.find(class_='rating_num').string
    img_url = movie.find('img').get('src')
    movies.append((name, rate, img_url))


def save_img(url, name):
    bytes = urllib.request.urlopen(url)
    with open(f'{name}.jpg', 'wb') as f:
        f.write(bytes.read())
        f.flush()


if __name__ == '__main__':
    ''' print douban top 250 movies '''
    start = time.clock()
    for i in range(10):
        url = f'https://movie.douban.com/top250?start={i*25}&filter='
        get_movies(url)

    for movie in movies:
        pass
        print(movie)
        # save_img(movie[2], movie[0])

    end = time.clock()
    print(end - start)
