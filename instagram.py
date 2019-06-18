import requests
from bs4 import BeautifulSoup

# test url of johnny daigo
url = "https://www.instagram.com/p/BwhVD2OBDvL/"
r = requests.get(url)
unparsedText = r.text
soup = BeautifulSoup(unparsedText)
print(soup)