import web
import urllib.request
import time
import csv
import json
import requests

# connect to MovieSite.db
db = web.database(dbn='sqlite', db='MovieSite.db')


# add movie info to database;
def add_movie(movie):
    movie = json.loads(data)
    # look up the process;
    print(movie['title'])

    db.insert('movie',
        id = int(movie['id']),
        title = movie['title'],
        origin = movie['original_title'],
        url = movie['alt'],
        rating = movie['rating']['average'],
        image = movie['images']['large'],
        directors = ','.join([d['name'] for d in movie['directors']]),
        casts = ','.join([c['name'] for c in movie['casts']]),
        year = movie['year'],
        genres = ','.join(movie['genres']),
        countries = ','.join(movie['countries']),
        summary = movie['summary'],
    )

# load movie_ids from csv file;
movie_ids = []
with open('movie_ids.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        movie_ids.append(row[0])

# according to movie_ids, add selected movie to our database;
count = 0
for i in movie_ids:
    print(count, i)
    response = requests.get('http://api.douban.com/v2/movie/subject/%s' % i)
    # some api page doesn't exist, BTW, most of them;
    if response.status_code != 200:
        continue
    data = response.text
    add_movie(data)
    count += 1
    time.sleep(3)
