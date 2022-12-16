with trip_station as (

    select 

    start_station_name,

    trip_month,

    subscription_type,

    count(trip_id) AS trip_counts

    from {{ ref('trip_station')}}

    group by 1, 2, 3
)

select * from trip_station