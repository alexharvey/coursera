import json
import urllib
import ssl

url = 'http://python-data.dr-chuck.net/comments_170695.json'
# serviceurl = int(raw_input('URL: '))

scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
uh = urllib.urlopen(url, context=scontext)
data = uh.read()


info = json.loads(data)
total = 0

for item in info['comments']:
    total += int(item['count'])
    # print 'Name', item['name']
    # print 'Count', item['count']

print total