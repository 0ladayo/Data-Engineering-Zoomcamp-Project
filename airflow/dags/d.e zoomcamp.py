#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd

import pyarrow

from datetime import datetime, timedelta

from google.cloud import bigquery

from airflow import DAG

from airflow.operators.python import PythonOperator


# In[4]:


default_args = {
    
    'owner': 'Oladayo',
    
    'retry': 1,
    
    'retry_delay': timedelta(minutes = 2)
}


# In[5]:


def file_names():
    
    files = ['trip', 'station','weather']
    
    return files


# In[7]:


def read_gcs_bucket_files():
    
    for file in file_names():
        
        df = pd.read_csv(f'gs://de-zoomcamp/{file}.csv')
        
        df.to_parquet(f'gs://de-zoomcamp2/{file}.parquet', engine = 'pyarrow')   


# In[7]:


def schema():
    
    schema_dic = {}
    
    schema_dic['trip'] = [
        
        {'name': 'id', 'type': 'INTEGER'}, {'name': 'duration', 'type': 'INTEGER'},
    
        {'name': 'start_date', 'type': 'STRING'}, {'name': 'start_station_name', 'type': 'STRING'},

        {'name': 'start_station_id', 'type': 'INTEGER'}, {'name': 'end_date', 'type': 'STRING'},

        {'name': 'end_station_name', 'type': 'STRING'}, {'name': 'end_station_id', 'type': 'INTEGER'},

        {'name': 'bike_id', 'type': 'INTEGER'}, {'name': 'subscription_type', 'type': 'STRING'},

        {'name': 'zip_code', 'type': 'STRING'}
    
    ]
    
    schema_dic['station'] = [
        
        {'name': 'id', 'type':'INTEGER'}, {'name': 'name', 'type':'STRING'}, {'name': 'lat', 'type':'FLOAT'}, 
    
        {'name': 'long', 'type':'FLOAT'}, {'name': 'dock_count', 'type':'INTEGER'}, {'name': 'city', 'type':'STRING'},

        {'name': 'installation_date', 'type':'STRING'}
    
    ]
    
    schema_dic['weather'] = [
        
        {'name': 'date', 'type': 'STRING'}, {'name': 'max_temperature_f', 'type': 'FLOAT'},
    
        {'name': 'mean_temperature_f', 'type': 'FLOAT'}, {'name': 'min_temperature_f', 'type': 'FLOAT'},

        {'name': 'max_dew_point_f', 'type': 'FLOAT'}, {'name': 'mean_dew_point_f', 'type': 'FLOAT'},

        {'name': 'min_dew_point_f', 'type': 'FLOAT'}, {'name': 'max_humidity', 'type': 'FLOAT'},

        {'name': 'mean_humidity', 'type': 'FLOAT'},{'name': 'min_humidity', 'type': 'FLOAT'},

        {'name': 'max_sea_level_pressure_inches', 'type': 'FLOAT'},{'name': 'mean_sea_level_pressure_inches', 'type': 'FLOAT'},

        {'name': 'min_sea_level_pressure_inches', 'type': 'FLOAT'}, {'name': 'max_visibility_miles', 'type': 'FLOAT'},

        {'name': 'mean_visibility_miles', 'type': 'FLOAT'}, {'name': 'min_visibility_miles', 'type': 'FLOAT'},

        {'name': 'max_wind_Speed_mph', 'type': 'FLOAT'}, {'name': 'mean_wind_speed_mph', 'type': 'FLOAT'},

        {'name': 'max_gust_speed_mph', 'type': 'FLOAT'}, {'name': 'precipitation_inches', 'type': 'STRING'},

        {'name': 'cloud_cover', 'type': 'FLOAT'}, {'name': 'events', 'type': 'STRING'},

        {'name': 'wind_dir_degrees', 'type': 'FLOAT'}, {'name': 'zip_code', 'type': 'INTEGER'}
    
    ]
    
    return schema_dic


# In[10]:


def load_to_query():

    client = bigquery.Client()
    
    for file in file_names():
        
        table_id = f'dummy-production-overview.de_datatset.{file}'
        
        job_config = bigquery.LoadJobConfig(
            
            schema = schema()[file],
            
            source_format = bigquery.SourceFormat.PARQUET,
        
        )
        
        url = f'gs://de-zoomcamp2/{file}.parquet'
        
        load_job = client.load_table_from_uri(
            
            url, table_id, job_config=job_config
        
        )
        
        load_job.result()
        
        destination_table = client.get_table(table_id)
        
        print("Loaded {} rows.".format(destination_table.num_rows))


# In[ ]:


with DAG(
    
    default_args = default_args, dag_id = 'de_pipeline', start_date = datetime(2022, 11,26)

) as dag:
    
    task1 = PythonOperator(
        
        task_id = 'file_names' , python_callable = file_names
    
    )
    
    task2 = PythonOperator(
        
        task_id = 'read_gcs_bucket_files', python_callable = read_gcs_bucket_files
    
    
    )
    
    task3 = PythonOperator(
        
        task_id = 'schema', python_callable = schema
    
    
    )
    
    task4 = PythonOperator(
        
        task_id = 'load_to_big_query', python_callable = load_to_query
    
    
    )
    
    task1 >> task2 >> task3 >> task4

