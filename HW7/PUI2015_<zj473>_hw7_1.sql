<<<<<<< HEAD:HW7/PUI2015_<zj473>_hw7_1.sql
{\rtf1\ansi\ansicpg1252\cocoartf1265\cocoasubrtf210
{\fonttbl\f0\fnil\fcharset134 STHeitiSC-Light;}
{\colortbl;\red255\green255\blue255;}
\margl1440\margr1440\vieww10380\viewh7200\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural

\f0\fs24 \cf0 SELECT\
 COUNT(tripduration) as trip_count,\
 start_station_id,\
 start_station_name,\
 end_station_id,\
 end_station_name\
\
FROM citibike\
\
GROUP BY start_station_id,start_station_name,end_station_id,end_station_name\
\
ORDER BY trip_count DESC}
=======

SELECT
 COUNT(tripduration) as trip_count,
 start_station_id,
 start_station_name,
 end_station_id,
 end_station_name

FROM citibike

GROUP BY start_station_id,start_station_name,end_station_id,end_station_name

ORDER BY trip_count DESC


>>>>>>> 11188607166c46b8b1043210a8bf2e806d8b1412:HW7/PUI2015_<zj473>_hw7_<Assignment1>.sql
