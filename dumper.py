from bs4 import BeautifulSoup

def extractPageData(pageAsTxt,storage):
    soup=BeautifulSoup(pageAsTxt,"lxml")

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

def extractMaxPages(pageAsTxt):
    soup=BeautifulSoup(pageAsTxt,"lxml")
    maxPages=soup.select("ol.nav li").pop().getText().strip()
    return int(maxPages)
