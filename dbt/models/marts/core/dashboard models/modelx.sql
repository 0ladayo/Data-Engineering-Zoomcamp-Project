with trip_station as (

    select

    trip_year,

    subscription_type,

    round(avg(trip_duration) / 60, 0) AS trip_duration,

    from {{ ref('trip_station')}}

    group by 1, 2

)

select * from trip_station