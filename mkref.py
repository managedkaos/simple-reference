from __future__ import print_function
import sys
import requests
from bs4 import BeautifulSoup

# process each command line argument as a URL
for url in sys.argv[1:]:

    # make a request to get the URL
    r = requests.get(url)

    # turn the request text into soup
    s = BeautifulSoup(r.text, "lxml")
    
    # print the simple reference with title and url
    print("\"%s\", %s" % (s.title.string, url))
