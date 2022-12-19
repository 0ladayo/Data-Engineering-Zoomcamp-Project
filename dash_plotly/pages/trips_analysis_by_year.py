import dash

from dash import callback, Input, Output

from read_big_query_tables import *

from plot_functions import *

from web_framework import *

dash.register_page(__name__, path='/', name='Yearly Overview')

layout = html.Div([

    dbc.Row([dbc.Col([html.Div([

    ])
    ], md=6),

        dbc.Col([html.Div([dbc.Col([html.Div([

            html.Label('SELECT A YEAR:',

                       style=style_1),

            html.Div(make_break(1)),

            dcc.Dropdown(id='trip year',

                         options=[{'label': i, 'value': i} for i in df_year['trip_year'].unique()],

                         value='2013',

                         style=style_2)

        ])

        ], md=4),

            dbc.Col([html.Div([

                html.Label('SELECT TRIP START OR END STATION:',

                           style=style_1),

                html.Div(make_break(1)),

                dcc.Dropdown(id='start or end',

                             options=[{'label': 'Start', 'value': 'Start'},

                                      {'label': 'End', 'value': 'End'}],

                             value='Start',

                             style=style_2)

            ])

            ], md=4),

            dbc.Col([html.Div([

                html.Label('SELECT A SUBSCRIPTION TYPE:',

                           style=style_1),

                html.Div(make_break(1)),

                dcc.Dropdown(id='subscription type',

                             options=[{'label': i, 'value': i} for i in df_year_subs['subscription_type'].unique()],

                             style=style_2)

            ])

            ], md=4)

        ], style=dict(display='flex'))

        ], md=6)

    ]),

    html.Div(make_break(2)),

    structure_1,

    html.Div(make_break(2)),

    structure_2,

    html.Div(make_break(3)),

    structure_3

])


@callback(
    Output('no of trips', 'children'),

    Output('average duration', 'children'),

    Output('no of stations', 'children'),

    Output('map', 'figure'),

    Output('bar chart 1', 'figure'),

    Output('bar chart 2', 'figure'),

    Input('trip year', 'value'),

    Input('start or end', 'value'),

    Input('subscription type', 'value'))
def plots(trip_year, start_or_end, subscription_type):

    if subscription_type==None:

        df_year_copy = df_year[(df_year['trip_year'] == trip_year) & (df_year['start_or_end'] == start_or_end)]

        df_year_copy2 = df_year[df_year['trip_year'] == trip_year]

        val = df_year_copy['trip_counts'].sum()

        val2 = df_trip_duration[df_trip_duration['trip_year'] == trip_year]['trip_duration']

        if df_year_copy2[df_year_copy2['start_or_end'] == 'Start']['station_name'].nunique() >= \
                df_year_copy2[df_year_copy2['start_or_end'] == 'End']['station_name'].nunique():

            val3 = df_year_copy2[df_year_copy2['start_or_end'] == 'Start']['station_name'].nunique()

        else:

            val3 = df_year_copy2[df_year_copy2['start_or_end'] == 'End']['station_name'].nunique()

        fig = plot_func(df_year_copy, hover_data=['trip_year', 'start_or_end', 'trip_counts'])

        df_month_copy = df_month[df_month['trip_year'] == trip_year]

        fig2 = plot_func2(df_month_copy)

        df_hour_copy = df_hour[df_hour['trip_year'] == trip_year]

        fig3 = plot_func3(df_hour_copy)

        return val, val2, val3, fig, fig2, fig3

    else:

        df_year_subs_copy = df_year_subs[(df_year_subs['trip_year'] == trip_year) & \

                                         (df_year_subs['start_or_end'] == start_or_end) & \

                                         (df_year_subs['subscription_type'] == subscription_type)]

        df_year_copy2 = df_year[df_year['trip_year'] == trip_year]

        val = df_year_subs_copy['trip_counts'].sum()

        val2 = df_trip_duration_subs[(df_trip_duration_subs['trip_year'] == trip_year) & \

                                     (df_trip_duration_subs['subscription_type'] == \

                                      subscription_type)]['trip_duration']

        if df_year_copy2[df_year_copy2['start_or_end'] == 'Start']['station_name'].nunique() >= \
                df_year_copy2[df_year_copy2['start_or_end'] == 'End']['station_name'].nunique():

            val3 = df_year_copy2[df_year_copy2['start_or_end'] == 'Start']['station_name'].nunique()

        else:

            val3 = df_year_copy2[df_year_copy2['start_or_end'] == 'End']['station_name'].nunique()

        fig = plot_func(df_year_subs_copy, hover_data=['subscription_type', 'trip_year', 'start_or_end',

                                                       'trip_counts', 'trip_counts'])

        df_month_subs_copy = df_month_subs[(df_month_subs['trip_year'] == trip_year) & \

                                           (df_month_subs['subscription_type'] == subscription_type)]

        fig2 = plot_func2(df_month_subs_copy)

        df_hour_subs_copy = df_hour_subs[(df_hour_subs['trip_year'] == trip_year) & \

                                         (df_hour_subs['subscription_type'] == subscription_type)]

        fig3 = plot_func3(df_hour_subs_copy)

        return val, val2, val3, fig, fig2, fig3