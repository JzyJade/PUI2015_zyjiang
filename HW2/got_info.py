# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 16:12:07 2015

@author: jiangzeyu
"""

import json
import sys
import urllib2
import csv

if __name__=='__main__':
    key = 'b5b223e6-110e-41a7-b0e0-b96f33c6e493'
    bus = 'B52'
    
    url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' %(key,bus)
    
    request = urllib2.urlopen(url)
    metadata = json.loads(request.read())
    
    nbus = metadata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
    number = len(nbus)
    
    with open(bus, 'wb') as csvFile:
        writer = csv.writer(csvFile)
        headers = ['Latitude','Longitude','Stop Name','Stop Status']
        writer.writerow(headers)
        
        for i in range(number):
            Latitude = nbus[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
            Longitude = nbus[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
            
            if nbus[i]['MonitoredVehicleJourney']['OnwardCalls'] == {}:
                StopName = 'N/A'
                StopStatus = 'N/A'
                
        else:
            StopName = nbus[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
            StopStatus = nbus[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions'] ['Distances']['PresentableDistance']
            
        
        writer.writerow([Latitude,Longitude,StopName,StopStatus])
            
        
            
                
                
                
                
            
            

        
   