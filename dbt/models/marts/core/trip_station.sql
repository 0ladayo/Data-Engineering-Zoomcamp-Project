with trip as (

    select

    trip_id,

    trip_duration,

    start_station_name,

    start_station_id,

    FORMAT_DATETIME("%F", end_date) AS trip_date,

    FORMAT_DATETIME("%Y", end_date) AS trip_year,

    FORMAT_DATETIME("%b", end_date) AS trip_month,

    CAST(FORMAT_DATETIME("%H", end_date) AS INT) + 1 AS trip_hour,

    end_station_name,
    
    end_station_id,

    subscription_type
    
    from {{ ref('stg_trip')}}

),

station as (

    select * from {{ ref('stg_station')}}

),

combined as (

    select 

    trip.trip_id,

    trip.trip_duration,

    trip.start_station_name,

    trip.start_station_id,

    trip.trip_date,

    trip.trip_year,

    trip.trip_month,

    trip.trip_hour,

    trip.end_station_name,

    trip.end_station_id,

    trip.subscription_type,

    station.station_lat AS end_station_lat,

    station.station_long AS end_station_long,

    station.city,

    station.installation_year

    from trip

    left join station 

    on trip.end_station_id = station.station_id

),

trip_station as (

    select

    combined.trip_id,

    combined.trip_duration,

    combined.start_station_name,

    combined.start_station_id,

    station.station_lat AS start_station_lat,

    station.station_long AS start_station_long,

    combined.trip_date,

    combined.trip_year,

    combined.trip_month,

    combined.trip_hour,

    combined.end_station_name,

    combined.end_station_id,

    combined.subscription_type,

    combined.end_station_lat,

    combined.end_station_long,

    combined.city,

    combined.installation_year

    from combined

    left join station

    on combined.start_station_id = station.station_id

)

select * from trip_station