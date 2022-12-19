#!/usr/bin/env python
# coding: utf-8

# In[21]:


import plotly.express as px


# In[22]:


api_token = 'pk.eyJ1IjoiMGxhZGF5byIsImEiOiJja3o4bXRlc2cweDE1MnVtdWJuZjBkMW1rIn0.Ulh37a4zmejYBzZ5Pfm8iw'


# In[23]:


def plot_func(df, hover_data):
    
    fig = px.scatter_mapbox(df, lat = 'station_lat', lon = 'station_long', hover_name = 'station_name',
                            
                            hover_data = hover_data, color = 'trip_counts', 
                            
                            color_continuous_scale = px.colors.sequential.Rainbow)
    
    fig.update_layout(
        
        mapbox = {'accesstoken': api_token, 'zoom': 10,'style':'dark'}, margin = dict(l = 0, r =0, t = 0, b = 0),
        
        height = 850,title_text = 'Trip Count Distribution by Bike Stations',
        
        title_x = 0.5, title_y = 0.98, title_font_color = 'rgb(255,255,255)', 
        
        paper_bgcolor = 'rgb(52,51,50)')
    
    fig.update_coloraxes(colorbar_tickfont_color = 'rgb(255, 255, 255)', 
                         
                         colorbar_title_font_color = 'rgb(255, 255, 255)')
    
    return fig


# In[24]:


def plot_func2(df):
    
    fig = px.bar(df, x = 'trip_month', y = 'trip_counts')
    
    fig.update_layout(title_text = 'Trip Count Distribution by Month', title_x = 0.5, title_y = 0.98, 
                      
                      title_font_color = 'rgb(255,255,255)',plot_bgcolor = 'rgb(52,51,50)', 
                      
                      paper_bgcolor = 'rgb(52,51,50)', yaxis = dict(color = 'rgb(255,255,255)'),
                      
                      xaxis = dict(color = 'rgb(255,255,255)'), margin = dict(l = 20, r = 20, t = 20, b = 20), 
                      
                      height = 600).update_traces(width = 0.3).update_yaxes(gridcolor = 'rgb(60, 64, 67)',
                                                                            
                                                                            title = 'Trip Count',
                                                                            
                                                                            rangemode='tozero',fixedrange=True).update_xaxes(title = 'Months', 
                                                                                                                      
                                                                                                                      categoryorder='array', categoryarray= ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        
                                                                                                                      fixedrange=True)
    
    return fig
        


# In[25]:


def plot_func3(df):
    
    fig = px.bar(df, x = 'trip_hour', y = 'trip_counts')
    
    fig.update_layout(title_text = 'Trip Count Distribution by Hour', title_x = 0.5, title_y = 0.98, 
                       
                       title_font_color = 'rgb(255,255,255)',plot_bgcolor = 'rgb(52,51,50)', 
                       
                       paper_bgcolor = 'rgb(52,51,50)', yaxis = dict(color = 'rgb(255,255,255)'),
                       
                       xaxis = dict(color = 'rgb(255,255,255)'), margin = dict(l = 20, r = 20, t = 20, b = 20), 
                       
                       height = 600).update_traces(width = 0.3).update_yaxes(gridcolor = 'rgb(60, 64, 67)',
                                                                             
                                                                             title = 'Trip Count',  rangemode='tozero', 
                                                                             
                                                                             fixedrange=True).update_xaxes(title = 'Hour of the Day',
                                                                                                           
                                                                                                           fixedrange=True)
    
    return fig

