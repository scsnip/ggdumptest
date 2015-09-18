def fileAsString(fileName):
    f=open(fileName,"r")
    data=f.read()
    f.close()
    return data

def test_extractMaxPages():
    """getting total pages number from first page"""
    from dumper import extractMaxPages
    data = fileAsString("video.html")
    maxPagesActual = extractMaxPages(data)
    maxPagesExpected = 147
    assert maxPagesExpected == maxPagesActual

def test_extractPageData():
    """parsing page data and checking if resulting data is populated"""
    from dumper import extractPageData
    data = fileAsString("video_page_1.html")
    storage = {}
    extractPageData(data,storage)
    actualSize = len(storage)
    expectedSize = 8
    assert expectedSize == actualSize

def test_extractPageData_containsKey():
    """parsing page data and checking if resulting data contains stream->url->title chain"""
    from dumper import extractPageData
    data = fileAsString("video_page_1.html")
    storage = {}
    extractPageData(data,storage)
    chunkForTest=storage["Neonavt"]["streams"][0]
    assert "failedStarCraft" in chunkForTest["title"]
