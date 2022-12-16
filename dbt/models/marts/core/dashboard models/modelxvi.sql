with trip_station as (

    select 

    start_station_name,

    trip_hour,

    count(trip_id) AS trip_counts

    from {{ ref('trip_station')}}

    group by 1, 2
)

select * from trip_station