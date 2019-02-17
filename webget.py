import os
import urllib.request as req
from urllib.parse import urlparse

def download(urls, to=None):
    for url in urls:
        filename = os.path.basename(url)
        if to == None:
            directory = "./" + filename
        else:
            directory = to
        if os.path.isfile(directory):
            print( "The file " + directory + " already exists")
        else:
            print("Downloading...", url)
            urlInfo = req.urlretrieve(url, directory)
            print("Succes! Printed To: " + directory)