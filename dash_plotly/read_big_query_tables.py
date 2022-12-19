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
    
    if '1' in model:
        
        df['start_or_end'] = 'End'
        
    elif '2' in model:
        
        df['start_or_end'] = 'Start'
        
    elif '3' in model:
        
        df['start_or_end'] = 'End'
        
    elif '4' in model:
        
        df['start_or_end'] = 'Start'
        
    else:
        
        pass
    
    df_copy = df.copy()
    
    return df_copy


# In[4]:


df_year = pd.concat([read_bq_table('model1'), read_bq_table('model2')], axis = 0)


# In[5]:


df_year_subs = pd.concat([read_bq_table('model3'), read_bq_table('model4')], axis = 0)


# In[6]:


df_hour = read_bq_table('model5')
    
df_hour_subs = read_bq_table('model7')


# In[7]:


df_month = read_bq_table('model6')

df_month_subs = read_bq_table('model8')


# In[8]:


df_trip_duration = read_bq_table('model9')

df_trip_duration_subs = read_bq_table('modelx')

