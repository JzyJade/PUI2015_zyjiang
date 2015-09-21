import datetime
import json
import sys
import urllib2

if _name_=='main_':
   for dataId in sys.argv[1:]: 
    url = 'https://nycopendata.socrata.com/views/%s' % (sys.argv[1])
    request = urlib2.urlopen(url)
    metadata = json.load(request.read())
   print dataId,datetime.datetime.fromtimestamp(metadate['createdAt'])
