# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 14:40:03 2015

@author: jiangzeyu
"""

import json
import sys
import urllib2


if __name__=='__main__':
    key = 'b5b223e6-110e-41a7-b0e0-b96f33c6e493'
    bus = 'B52'
    
    url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' %(key,bus)
    
    request = urllib2.urlopen(url)
    metadata = json.loads(request.read())
    
    nbus = metadata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
    number = len(nbus)
    
    print "Bus Line: %s" %(bus)
    print "Number of Bus: %s" %(number)
    

    for i in range(number):
        Lati = nbus[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
        Long = nbus[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
        print 'Bus %s is at latitude %s and longitude %s' % (i, Lati, Long)
        
        
        