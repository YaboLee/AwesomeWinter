import csv
import urllib.request
import requests
import json
import web
import time


def get_poster(id, url):
    file_name = 'poster/%d.jpg' % id
    pic = urllib.request.urlretrieve(url, file_name)

db = web.database(dbn='sqlite', db='MovieSite.db')
movies = db.select('movie')

count = 0
for movie in movies:
    get_poster(movie.id, movie.image)
    count += 1
    print(count, movie.title)
    time.sleep(2)
