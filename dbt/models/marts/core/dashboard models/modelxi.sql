with trip_station as (

    select

    trip_id,
    
    round((trip_duration) / 60, 0) AS trip_duration,

    start_station_name,

    trip_date,

    trip_month,

    trip_hour,

    end_station_name,

    end_station_lat,

    end_station_long,

    subscription_type

    from {{ ref('trip_station')}}

)

select * from trip_station