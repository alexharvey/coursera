import json
import urllib
import ssl

endpoint = 'http://python-data.dr-chuck.net/geojson?'
# serviceurl = int(raw_input('URL: '))

address = 'University of Michigan'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = endpoint + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'

    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
        print data
        continue

    print json.dumps(js, indent=4)

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print 'lat',lat,'lng',lng
    location = js['results'][0]['formatted_address']
    print location

