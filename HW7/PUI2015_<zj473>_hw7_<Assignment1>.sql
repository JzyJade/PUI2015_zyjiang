
SELECT
 COUNT(tripduration) as trip_count,
 start_station_id,
 start_station_name,
 end_station_id,
 end_station_name

FROM citibike

GROUP BY start_station_id,start_station_name,end_station_id,end_station_name

ORDER BY trip_count DESC


