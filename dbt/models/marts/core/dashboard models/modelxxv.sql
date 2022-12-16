with trip_station as (
    
    select 

    start_station_name,

    end_station_name AS station_name,

    end_station_lat AS station_lat,

    end_station_long AS station_long,

    subscription_type,

    trip_year,

    count(trip_id) AS trip_counts,

    from {{ ref('trip_station')}}

    group by 1, 2, 3, 4, 5, 6
    
)

select * from trip_station