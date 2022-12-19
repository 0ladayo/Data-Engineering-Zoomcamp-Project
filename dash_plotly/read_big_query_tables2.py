#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

import os

import pandas_gbq

from google.cloud import bigquery


# In[2]:


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'dummy-production-overview-b47377a83f9e.json'


# In[3]:


def read_bq_table(model):
    
    query_string = f"SELECT * FROM `dummy-production-overview.dbt_de_dataset.{model}` "
    
    df = pandas_gbq.read_gbq(query_string, project_id = 'dummy-production-overview')
    
    df_copy = df.copy()
    
    return df_copy


# In[4]:


df_start_station = read_bq_table('modelxii')

df_start_station_subs = read_bq_table('modelxiii')

df_start_station_year = read_bq_table('modelxx')

df_start_station_comb = read_bq_table('modelxxv')


# In[5]:


df_month = read_bq_table('modelxiv')

df_month_subs = read_bq_table('modelxv')

df_month_year = read_bq_table('modelxxi')

df_month_comb = read_bq_table('modelxxvi')


# In[6]:


df_hour = read_bq_table('modelxvi')

df_hour_subs = read_bq_table('modelxvii')

df_hour_year = read_bq_table('modelxxiii')

df_hour_comb = read_bq_table('modelxxvii')


# In[7]:


df_trip_duration = read_bq_table('modelxviii')

df_trip_duration_subs = read_bq_table('modelxix')

df_trip_duration_year = read_bq_table('modelxxiv')

df_trip_duration_comb = read_bq_table('modelxxviii')

