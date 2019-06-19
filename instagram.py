import requests
from bs4 import BeautifulSoup

# test url of johnny daigo
url = "https://www.instagram.com/p/BwhVD2OBDvL/"
r = requests.get(url)
unparsedText = r.text
soup = BeautifulSoup(unparsedText, "html.parser")
metas = soup.find_all('meta')
# img = metas.find(property="og:image")
img = soup.find('meta',{'property' : 'og:image'})
print(img.attrs['content'])