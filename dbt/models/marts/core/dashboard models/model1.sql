with trip_station as (

    select
    
    end_station_name AS station_name,

    end_station_lat AS station_lat,

    end_station_long AS station_long,

    trip_year,

    count(trip_id) AS trip_counts,

    from {{ ref('trip_station')}}

     group by 1, 2, 3, 4

)

select * from trip_station