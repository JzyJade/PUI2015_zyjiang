<<<<<<< HEAD:HW7/PUI2015_<zj473>_hw7_2.sql
{\rtf1\ansi\ansicpg1252\cocoartf1265\cocoasubrtf210
{\fonttbl\f0\fnil\fcharset134 STHeitiSC-Light;}
{\colortbl;\red255\green255\blue255;}
\margl1440\margr1440\vieww10380\viewh7200\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural

\f0\fs24 \cf0 SELECT \
	start_station_id, \
	start_station_name,	CDB_TransformToWebmercator(CDB_LatLng(\
  start_station_latitude, \
  start_station_longitude)) \
as the_geom_webmercator, \
COUNT(tripduration) AS trip_count \
\
FROM citibike \
\
WHERE \
	ST_Dwithin(\
      	CDB_LatLng(\
  			 start_station_latitude,\
        start_station_longitude\
)::geography,\
       CDB_LatLng(40.7307602,-73.9974086)::geography,\
           1000)\
AND\
extract(DOW FROM starttime) IN (0,6)\
\
GROUP BY\
start_station_id,\
start_station_name,\
start_station_latitude,\
start_station_longitude\
\
ORDER BY trip_count DESC}
=======


SELECT 
	start_station_id, 
	start_station_name,	CDB_TransformToWebmercator(CDB_LatLng(
  start_station_latitude, 
  start_station_longitude)) 
as the_geom_webmercator, 
COUNT(tripduration) AS trip_count 

FROM citibike 

WHERE 
	ST_Dwithin(
      	CDB_LatLng(
  			 start_station_latitude,
        start_station_longitude
)::geography,
       CDB_LatLng(40.7307602,-73.9974086)::geography,
           1000)
AND
extract(DOW FROM starttime) IN (0,6)


GROUP BY
start_station_id,
start_station_name,
start_station_latitude,
start_station_longitude

ORDER BY trip_count DESC





>>>>>>> 11188607166c46b8b1043210a8bf2e806d8b1412:HW7/PUI2015_<zj473>_Assignment2.sql
