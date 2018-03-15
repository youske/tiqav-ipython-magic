from IPython.display import Image
import os,json
import requests

def imfeeling(word):
    try:
      return Image(url="http://%s.tiqav.com" % (word))  
    except ValueError as e:
      raise e

def load_ipython_extension(ipython):
    ipython.register_magic_function(imfeeling, 'line')

if __name__ == '__main__':
    imfeeling('xxx')

