# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
import json
import ssl
from BeautifulSoup import *

# url = raw_input('URL: ')
# url = 'https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html'
url = 'https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Suzy.html'
count = int(raw_input('Count: '))
position = int(raw_input('Position: '))
print 'Retrieving', url
scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
uh = urllib.urlopen(url, context=scontext)
html = uh.read()
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('a')
# print tags

tag = tags[position-1]
for i in range(0, count):
    print 'Retrieving', tag.get('href', None)
    scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    uh = urllib.urlopen(tag.get('href', None), context=scontext)
    html = uh.read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    tag = tags[position-1]


