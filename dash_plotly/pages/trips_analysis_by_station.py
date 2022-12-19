import dash

from dash import callback, Input, Output

from read_big_query_tables2 import *

from plot_functions import *

from web_framework2 import *

from styling import *

dash.register_page(__name__, name='Station Overview')

layout = html.Div([

    dbc.Row([dbc.Col([html.Div([

    ])
    ], md=7),

        dbc.Col([html.Div([dbc.Col([html.Div([

            html.Label('SELECT A START STATION:',

                       style=style_1),

            html.Div(make_break(1)),

            dcc.Dropdown(id='start_station',

                         options=[{'label': i, 'value': i} for i in
                                  df_start_station_subs['start_station_name'].unique()],

                         value=df_start_station_subs['start_station_name'].iloc[0],

                         style={**style_2, 'width': '75%'})

        ])

        ], md=4),

            dbc.Col([html.Div([

                html.Label('SELECT A SUBSCRIPTION TYPE:',

                           style=style_1),

                html.Div(make_break(1)),

                dcc.Dropdown(id='subscription_type',

                             options=[{'label': i, 'value': i} for i in df_start_station_subs['subscription_type']\
                             .unique()],

                             style={**style_2, 'width': '75%'})

            ])

            ], md=4),

            dbc.Col([html.Div([

                html.Label('SELECT A YEAR:',

                           style=style_1),

                html.Div(make_break(1)),

                dcc.Dropdown(id='year_',

                             options=[{'label': i, 'value': i} for i in df_start_station_year['trip_year'].unique()],

                             style={**style_2, 'width': '75%'})

            ])

            ], md=4)

        ], style=dict(display='flex'))

        ], md=5)

    ]),

    html.Div(make_break(2)),

    structure_1,

    html.Div(make_break(2)),

    structure_2,

    html.Div(make_break(3)),

    structure_3

])


@callback(

    Output('no_of_trips', 'children'),

    Output('average_duration', 'children'),

    Output('no_of_stations', 'children'),

    Output('map_', 'figure'),

    Output('bar_chart_1', 'figure'),

    Output('bar_chart_2', 'figure'),

    Input('start_station', 'value'),

    Input('subscription_type', 'value'),

    Input('year_', 'value'))
def plot(start_station, subscription_type, year):
    if subscription_type == None and year == None:

        df_start_station_copy = df_start_station[df_start_station['start_station_name'] == start_station]

        val = df_start_station_copy['trip_counts'].sum()

        val1 = df_trip_duration[df_trip_duration['start_station_name'] == start_station]['trip_duration']

        val2 = df_start_station_copy['station_name'].nunique()

        fig = plot_func(df_start_station_copy, hover_data=['station_name', 'trip_counts'])

        df_month_copy = df_month[df_month['start_station_name'] == start_station]

        fig1 = plot_func2(df_month_copy)

        df_hour_copy = df_hour[df_hour['start_station_name'] == start_station]

        fig2 = plot_func3(df_hour_copy)

        return val, val1, val2, fig, fig1, fig2

    elif year == None:

        df_start_station_subs_copy = df_start_station_subs[
            (df_start_station_subs['start_station_name'] == start_station) & \

            (df_start_station_subs['subscription_type'] == subscription_type)]

        val = df_start_station_subs_copy['trip_counts'].sum()

        val1 = df_trip_duration_subs[(df_trip_duration_subs['start_station_name'] == start_station) & \

                                     (df_trip_duration_subs['subscription_type'] == subscription_type)]['trip_duration']

        val2 = df_start_station_subs_copy['station_name'].nunique()

        fig = plot_func(df_start_station_subs_copy, hover_data=['station_name', 'subscription_type', 'trip_counts'])

        df_month_subs_copy = df_month_subs[(df_month_subs['start_station_name'] == start_station) & \

                                           (df_month_subs['subscription_type'] == subscription_type)]

        fig1 = plot_func2(df_month_subs_copy)

        df_hour_subs_copy = df_hour_subs[(df_hour_subs['start_station_name'] == start_station) & \

                                         (df_hour_subs['subscription_type'] == subscription_type)]

        fig2 = plot_func3(df_hour_subs_copy)

        return val, val1, val2, fig, fig1, fig2

    elif subscription_type == None:

        df_start_station_year_copy = df_start_station_year[
            (df_start_station_year['start_station_name'] == start_station) & \

            (df_start_station_year['trip_year'] == year)]

        val = df_start_station_year_copy['trip_counts'].sum()

        val1 = df_trip_duration_year[(df_trip_duration_year['start_station_name'] == start_station) &\

                                     (df_trip_duration_year['trip_year'] == year)]['trip_duration']

        val2 = df_start_station_year_copy['station_name'].nunique()

        fig = plot_func(df_start_station_year_copy, hover_data=['station_name', 'trip_year', 'trip_counts'])

        df_month_year_copy = df_month_year[(df_month_year['start_station_name'] == start_station) &\

                                           (df_month_year['trip_year'] == year)]

        fig1 = plot_func2(df_month_year_copy)

        df_hour_year_copy = df_hour_year[(df_hour_year['start_station_name'] == start_station) &\

                                         (df_hour_year['trip_year'] == year)]

        fig2 = plot_func3(df_hour_year_copy)

        return val, val1, val2, fig, fig1, fig2

    else:

        df_start_station_comb_copy = df_start_station_comb[
            (df_start_station_comb['start_station_name'] == start_station) &\

            (df_start_station_comb['subscription_type'] == subscription_type) &\

            (df_start_station_comb['trip_year'] == year)]

        val = df_start_station_comb_copy['trip_counts'].sum()

        val1 = df_trip_duration_comb[(df_trip_duration_comb['start_station_name'] == start_station) &\

                                     (df_trip_duration_comb['subscription_type'] == subscription_type) &\

                                     (df_trip_duration_comb['trip_year'] == year)]['trip_duration']

        val2 = df_start_station_comb_copy['station_name'].nunique()

        fig = plot_func(df_start_station_comb_copy, hover_data=['station_name', 'trip_counts', 'trip_year',

                                                                'subscription_type'])

        df_month_comb_copy = df_month_comb[(df_month_comb['start_station_name'] == start_station) &\

                                           (df_month_comb['subscription_type'] == subscription_type) &\

                                           (df_month_comb['trip_year'] == year)]

        fig1 = plot_func2(df_month_comb_copy)

        df_hour_comb_copy = df_hour_comb[(df_hour_comb['start_station_name'] == start_station) &\

                                         (df_hour_comb['subscription_type'] == subscription_type) &\

                                         (df_hour_comb['trip_year'] == year)]

        fig2 = plot_func3(df_hour_comb_copy)

        return val, val1, val2, fig, fig1, fig2
