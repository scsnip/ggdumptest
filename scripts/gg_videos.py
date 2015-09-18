# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import json
import codecs

def grabDataFromPage(urlToGrab,storage):
	global f
	r=requests.get(urlToGrab)
	r.encoding="UTF-8"
	soup=BeautifulSoup(r.text,"lxml")

	for block in soup.select(".video_block"):
		title=block.select(".title a").pop().getText().strip()
		url=block.select(".title a").pop().get("href").strip()
		author=block.select(".video_autor a").pop().getText().strip()
		if storage.has_key(author):
			d=storage[author]
			streams=d["streams"]
			streams.append({"title":title,"url":url})
		else:
			storage[author]={"streams":[{"title":title,"url":url}]}

startUrl="http://goodgame.ru/video/"
page='http://goodgame.ru/video/page/%s/'

soup=BeautifulSoup(requests.get(startUrl).text,"lxml")
maxPages=soup.select("ol.nav li").pop().getText().strip()
crawledData={}

for i in range(1,int(maxPages)+1):
# for i in range(1,5):
	print "Grabbing %s page"%i
	grabDataFromPage(page%i,crawledData)

f=codecs.open("res.html","w+","UTF-8")

streamers=crawledData.keys()
for s in sorted(streamers):
	count=len(crawledData[s]["streams"])
	f.write("<a href='#%s'>%s %s</a><br>"%(s,s,count))

for k in streamers:
	f.write("<a name='%s'></a>"%k)
	f.write("<h1>%s</h1>"%k)
	for stream in crawledData[k]["streams"]:
		f.write("<br>")
		f.write("<a href='%s' target='_blank'>%s</a>"%(stream["url"],stream["title"]))

f.close()