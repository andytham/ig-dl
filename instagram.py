import requests
from bs4 import BeautifulSoup

# test url of johnny daigo
# url = "https://www.instagram.com/p/BwhVD2OBDvL/"

def grabUrl(url):
    r = requests.get(url)
    unparsedText = r.text
    soup = BeautifulSoup(unparsedText, "html.parser")
    # print(soup)
    imgUrl = soup.find('meta',{'property' : 'og:image'}).attrs['content']
    # get the extension
    ext = imgUrl.split('?')[0].split('.')[-1]
    # get author
    fullUrl = soup.find('link', {'rel' : 'canonical'}).attrs['href']
    author = fullUrl.split("/")[3]
    # get hash
    imgHash = fullUrl.split("/")[5]

    combinedName = author + " - " + imgHash

    #TODO check if mp4
    

    # soup to text for debugging purposes
    with open("test/test.html", "w", encoding='utf-8') as file:
        file.write(str(soup))

    print (imgUrl)
    print(combinedName)
    return [requests.get(imgUrl), ext, combinedName]

grabUrl("https://www.instagram.com/p/BwhVD2OBDvL/")