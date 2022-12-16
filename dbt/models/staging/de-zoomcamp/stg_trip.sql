with trip as (
    
    select 
    
    id AS trip_id,

    duration AS trip_duration,

    start_station_name,

    start_station_id,
    
    PARSE_DATETIME('%m/%d/%Y %H:%M', end_date) AS end_date,

    end_station_name,

    end_station_id,

    subscription_type,

    from {{ source('de-zoomcamp-project','trip')}}
    
    )

select 

trip_id,

trip_duration,

start_station_name,

start_station_id,

datetime(end_date) AS end_date,

end_station_name,

end_station_id,

subscription_type,

from trip