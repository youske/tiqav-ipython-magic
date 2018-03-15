from IPython.display import Image

import os,json
import requests

API_ENDPOINT = 'http://api.tiqav.com/search.json'

def tiqav(tag):
    images=[]
    url="%s?q=%s" % (API_ENDPOINT,tag)
    try:
        r = requests.get(url)
        tiqd=r.json()
        json = r.json()
        data = json
        for dt in data:
            if 'source_url' in dt:
                images.append( Image(url=dt['source_url']) )
    except ValueError as e:
        raise e
  
    return images

def load_ipython_extension(ipython):
    ipython.register_magic_function(tiqav, 'line')

if __name__ == '__main__':
    tiqav('xxx')

