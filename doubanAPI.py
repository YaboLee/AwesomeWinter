import urllib.request
import json
import time
import csv
import requests

# response = urllib.request.urlopen('http://api.douban.com/v2/movie/top250')
# data = response.read()
# data_json = json.loads(data)
# movie250 = data_json['subjects']
# for movie in movie250:
#     print(movie['id'], movie['title'])

# save movie_ids
movie_ids = []

for index in range(0, 250, 50):
    print(index)
    # Douban api can receive two parameters: start and count, start from specific one and list following count numbers;
    response = requests.get('http://api.douban.com/v2/movie/top250?start=%d&count=50'%index)
    data = response.text
    #print(data)
    # analyse with json;
    data_json = json.loads(data)
    movie250 = data_json['subjects']
    for movie in movie250:
        movie_ids.append(movie['id'])
        print(movie['id'], movie['title'])
    time.sleep(3)
# save to csv file;
myFile = open('movie_ids.csv','w')
# wr = csv.writer(myFile, delimiter=',')
for item in movie_ids:
    myFile.write("%s\n" %item)
myFile.close()

print(movie_ids)
