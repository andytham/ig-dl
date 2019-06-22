import requests
from bs4 import BeautifulSoup
import json, re

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
    #TODO if album

    # window._sharedData.entry_data.PostPage[0].graphql.shortcode_media.edge_sidecar_to_children.edges
    # loops through edges to each node
    # Use graphql? or just json?
    graphqlJson = soup.findAll(text=re.compile("window._sharedData"))[0][21:-1].encode(encoding='UTF-8',errors='strict')
    # print(graphqlJson)
    jsonDump = json.loads(graphqlJson)
    edges = jsonDump['entry_data']['PostPage'][0]['graphql']['shortcode_media']['edge_sidecar_to_children']['edges']
    imgList = []
    for node in edges:
        imgList.append(requests.get(node['node']['display_url']))

    #TODO check if mp4
    

    # soup to text for debugging purposes
    with open("test/test.html", "w", encoding='utf-8') as file:
        file.write(str(soup))

    print (imgUrl)
    print(combinedName)
    return [imgList, ext, combinedName]

import env
grabUrl(env.san)