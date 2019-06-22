import requests
from bs4 import BeautifulSoup

# test url of johnny daigo
# url = "https://www.instagram.com/p/BwhVD2OBDvL/"

def grabUrl(url):
    r = requests.get(url)
    unparsedText = r.text
    soup = BeautifulSoup(unparsedText, "html.parser")
    imgUrl = soup.find('meta',{'property' : 'og:image'}).attrs['content']
    # get the extension
    ext = imgUrl.split('?')[0].split('.')[-1]
    # get title of the post
    postTitle = soup.find('title').get_text()
    postTitle = postTitle.split(' on Instagram: ')[0] + ' - ' + postTitle.split(' on Instagram: ')[1]
    postTitle = postTitle.rstrip().lstrip()
    print(repr(postTitle))
    print (imgUrl)
    return [requests.get(imgUrl), ext, postTitle]

# grabUrl("https://www.instagram.com/p/BwhVD2OBDvL/")