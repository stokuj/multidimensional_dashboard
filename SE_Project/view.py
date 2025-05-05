# from ViewFolder.dashServer import*

# noinspection PyMethodMayBeStatic

from dash.dependencies import Input, Output, State
import dash
from dash import dcc
from dash import html
from dash import dash_table
import dash_bootstrap_components as dbc
from dash import html


class View:

    def _init_view(self, controller):
        self.controller = controller


    @staticmethod
    def set_name(app, name):
        app.title = name

    @staticmethod
    def set_layout(app):
        tabs_styles = {
            'height': '44px'
        }
        tab_style = {
            'borderBottom': '1px solid #d6d6d6',
            'padding': '6px',
            'fontWeight': 'bold'
        }

        tab_selected_style = {
            'borderTop': '1px solid #d6d6d6',
            'borderBottom': '1px solid #d6d6d6',
            'backgroundColor': '#119DFF',
            'color': 'white',
            'padding': '6px'
        }

        app.layout = html.Div([
            html.Br(),
            html.H1('Multidimensional Data Visualization',
                    style={
                        "textAlign": "center",
                    }
                    ),
            html.Br(),
            dcc.Tabs([
                dcc.Tab(style=tab_style, selected_style=tab_selected_style, label='Program', children=[
                    html.Br(),
                    dcc.Upload(
                        id="upload-data",
                        children=html.Div(["Drag and Drop or ", html.A("Select Files")]),
                        style={
                            "color": "red",
                            "width": "100%",
                            "height": "60px",
                            "lineHeight": "60px",
                            "borderWidth": "1px",
                            "borderStyle": "dashed",
                            "borderRadius": "5px",
                            "textAlign": "center",
                            "margin": "0px",
                        },
                        multiple=True,
                    ),
                    html.Br(),
                    dcc.Graph(id="Mygraph"),
                    html.Div(id="output-data-upload"),
                ]),
                dcc.Tab(style=tab_style, selected_style=tab_selected_style, label='Settings', children=[
                    html.Br(),
                    dcc.ConfirmDialog(
                        id='confirm-danger',
                        message='Are u sure?',
                    ),
                    dcc.Dropdown(
                        options=[
                            {'label': i, 'value': i}
                            for i in ['Parallel Coordinates', 'Parallel Categories']
                        ],
                        value='Parallel Coordinates',
                        id='dropdown-danger'
                    ),
                ]),
            ]),


        ])
