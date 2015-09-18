# -*- coding: utf-8 -*-
import requests
import json
import codecs
import dumper

RESULT_FILE="./gg.html"

def grabDataFromPage(urlToGrab,storage):
        global f
        r=requests.get(urlToGrab)
        r.encoding="UTF-8"
        dumper.extractPageData(r.text,storage)


def main():
        
        startUrl="http://goodgame.ru/video/"
        page='http://goodgame.ru/video/page/%s/'
        maxPages=dumper.extractMaxPages(requests.get(startUrl).text)
        crawledData={}

        for i in range(1,int(maxPages)+1):
                # for i in range(1,5):
                print "Grabbing %s page"%i
                grabDataFromPage(page%i,crawledData)
                
        f=codecs.open(RESULT_FILE,"w+","UTF-8")
        f.write('<head><meta charset="UTF-8"></head>')

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

if __name__=="__main__":
        main()
