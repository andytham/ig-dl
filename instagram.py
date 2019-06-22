import requests
from bs4 import BeautifulSoup
import json, re

def scrapeUrl(url):
    # soup
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    # soup to html for debugging purposes
    with open("test/soup.html", "w", encoding='utf-8') as file:
        file.write(str(soup))

    # create the file name to save as
    postTitle = soup.find('link', {'rel' : 'canonical'}).attrs['href']
    splitTitle = postTitle.split("/")
    filename = splitTitle[3] + " - " + splitTitle[5] # author + ig's hash
        
    # data is structured like this if in an album: window._sharedData.entry_data.PostPage[0].graphql.shortcode_media.edge_sidecar_to_children.edges
    # loops through edges to each node if album
    jsonData = soup.findAll(text=re.compile("window._sharedData"))[0][21:-1].encode(encoding='UTF-8',errors='strict')
    jsonDump = json.loads(jsonData)
    req = {'filename': filename} # what we will return, starting with the filename
    fileList = []
    # if album, else dump in single url
    shorthandJson = jsonDump['entry_data']['PostPage'][0]['graphql']['shortcode_media']
    def parseJsonIntoUrl(url):
        if url['is_video']:
            ext = url['video_url'].split('?')[0].split('.')[-1]
            mediaReqData = requests.get(url['video_url'])
            fileList.append([mediaReqData, ext])
        else:
            ext = url['display_url'].split('?')[0].split('.')[-1]
            mediaReqData = requests.get(url['display_url'])
            fileList.append([mediaReqData, ext])

    if 'edge_sidecar_to_children' in shorthandJson: # if it is an album (multi images)
        edges = shorthandJson['edge_sidecar_to_children']['edges']
        for node in edges:
            url = node['node']
            parseJsonIntoUrl(url)
    else:
        parseJsonIntoUrl(shorthandJson)
    req.update({'fileList':fileList})
    return req
  
# import env
# grabUrl(env.video)