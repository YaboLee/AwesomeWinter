import csv
import urllib.request
import requests
import json
import web
import time

#
# l = ['ads', 'sadfas', 'safas','wdq']
#
# theFile = open('movie_ids.csv', 'w')
# for i in l:
#     theFile.write("%s\n" %i)

# data = []
#
# with open('movie_ids.csv', 'r') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         data.append(row[0])
#
# print(data)

# html = urllib.request.urlopen('http://api.douban.com/v2/movie/subject/5912992')
# html = requests.get('http://api.douban.com/v2/movie/subject/5912992')
html = requests.get('http://api.douban.com/v2/movie/subject/1300267')
# j_data = json.loads(html.text)
# print(html.status_code)

html = requests.get('http://api.douban.com/v2/movie/top250?start=0&count=50')
# print(html.text)
data = json.loads(html.text)
# print(data['subjects'])

def get_poster(id, url):
    file_name = 'poster/%d.jpg' % id
    pic = urllib.request.urlretrieve(url, file_name)

    # f = open(file_name, 'wb')
    # f.write(pic)
    # f.close()

db = web.database(dbn='sqlite', db='MovieSite.db')
movies = db.select('movie')

count = 0
for movie in movies:
    get_poster(movie.id, movie.image)
    count += 1
    print(count, movie.title)
    time.sleep(2)
