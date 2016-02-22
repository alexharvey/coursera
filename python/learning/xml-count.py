import urllib
import ssl
import xml.etree.ElementTree as ET

# url = 'http://python-data.dr-chuck.net/comments_42.xml'
url = 'http://python-data.dr-chuck.net/comments_170691.xml'
# serviceurl = int(raw_input('URL: '))

scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
uh = urllib.urlopen(url, context=scontext)
data = uh.read()

tree = ET.fromstring(data)
counts = tree.findall('.//count')
total = 0
for c in counts:
    total += int(c.text)

print total