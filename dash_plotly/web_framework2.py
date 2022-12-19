#!/usr/bin/env python
# coding: utf-8

# In[1]:


from dash import dcc, html

from styling import *

import dash_bootstrap_components as dbc


# In[2]:


def make_break(num_breaks):
    
    br_list = ([html.Br()]*num_breaks)
    
    return br_list


# In[6]:


structure_1 = dbc.Row([dbc.Col([html.Div([html.Span(id = 'no_of_trips',
                                                      
                                                      style = {**style_1, 'font-size':'34px'}),
                                             
                                             html.Div(make_break(2)),
                                             
                                             html.Span('No of Trips',
                                                      
                                                      style = {**style_1, 'font-size':'13.6px'})
                                            
                                            ], style = style_3)
                                  
                                  ],  md = 1),
                          
                          dbc.Col([html.Div([html.Span(id = 'average_duration',
                                                       
                                                       style = {**style_1, 'font-size':'34px'}),
                                             
                                            html.Div(make_break(2)),
                                             
                                             html.Span('Average Duration (mins)',
                                                      
                                                      style = {**style_1, 'font-size':'13.6px'})
                                            
                                            ], style = style_3)
                                  
                                  ],  md = 1),
                       
                       dbc.Col([html.Div([html.Span(id = 'no_of_stations',
                                                       
                                                       style = {**style_1, 'font-size':'34px'}),
                                             
                                            html.Div(make_break(2)),
                                             
                                             html.Span('No of End Stations',
                                                      
                                                      style = {**style_1, 'font-size':'13.6px'})
                                            
                                            ], style = style_3)
                                  
                                  ],  md = 1)
                          
                         ])


# In[4]:


structure_2 = dbc.Row([dbc.Col([html.Div(
    
    dcc.Graph(id = 'map_'))
                 
                 ], md = 12)
        
        ])


# In[5]:


structure_3 = dbc.Row([dbc.Col([html.Div(
    
    dcc.Graph(id = 'bar_chart_1'))
                 
                 ], md = 4),
         
         dbc.Col([html.Div(
             
             dcc.Graph(id = 'bar_chart_2')
         
         )
                 
                 ], md = 8)
        
        ])


# In[ ]:




