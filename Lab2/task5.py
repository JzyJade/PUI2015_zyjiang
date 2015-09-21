import datetime
import json
import sys
import urllib2

if __name__=='__main__':
   jsonFile = open(sys.argv[1], 'r')
    data = json.load(jsonFile)
    stations = data['stationBeanList']

     with open(sys.argv[2], 'w') as csvFile:
        writer = csv.writer(csvFile)
        headers = ['Station Name' , 'Latitude', 'Longitude']
        writer.writerow(headers)

        for s in stations:
            if s ['statusKey']!=1 and s ['stationName'].startswith('Coming soon'):
                 stationNmae = s['stationName']
                 stationLat = s['latitution']

                 writer.writerow([stationName, stationLat, stationLon])
