with station as (

    select 
    
    id AS station_id,

    name AS station_name,

    lat AS station_lat,

    long AS station_long,

    city,

    PARSE_DATE('%m/%d/%Y', installation_date) AS installation_date

    from {{ source('de-zoomcamp-project','station')}}

    )

select 

station_id,

station_name,

station_lat,

station_long,

city,

EXTRACT(YEAR FROM installation_date) AS installation_year

from station