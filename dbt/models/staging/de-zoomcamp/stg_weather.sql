with weather as(

    select

    PARSE_DATE('%m/%d/%Y', date) AS weather_date,
    
    mean_temperature_f,

    mean_dew_point_f,

    mean_humidity,

    mean_visibility_miles,

    mean_wind_speed_mph,

    zip_code

    from {{ source('de-zoomcamp-project','weather')}}

    )

select 

* 

from weather