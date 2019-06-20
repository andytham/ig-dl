import requests
from bs4 import BeautifulSoup

# test url of johnny daigo
# url = "https://www.instagram.com/p/BwhVD2OBDvL/"

def grabUrl(url):
    r = requests.get(url)
    unparsedText = r.text
    soup = BeautifulSoup(unparsedText, "html.parser")
    imgUrl = soup.find('meta',{'property' : 'og:image'}).attrs['content']
    return requests.get(imgUrl)