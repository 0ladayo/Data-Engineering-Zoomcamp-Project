import dash

from dash import html

import dash_bootstrap_components as dbc

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

sidebar = html.Div(
    [
        html.Div(
            [
                html.H2('SF Bay Area Bike Share', style={"color": "white"}),
            ],
            className="sidebar-header",
        ),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink(

                    [

                        html.Div(page['name'])

                    ],

                    href=page['path'],
                    active='exact',

                )

                for page in dash.page_registry.values()

            ],
            vertical=True,
            pills=True,
        ),
    ],
    className="sidebar",
)

app.layout = dbc.Container(

    [sidebar, dash.page_container],

    fluid = True
)

if __name__ == "__main__":
    app.run_server(port = 8022, debug=True)