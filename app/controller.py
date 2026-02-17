from .model import Model
from .view import View
from pathlib import Path
from threading import Thread
import socket
import os
import requests

import plotly.graph_objects as go
import plotly.express as px
from dash import html
from dash import dash_table
import eel
from dash.dependencies import Input, Output, State
from flask import request
import pandas as pd
# noinspection PyMethodMayBeStatic

ModelObj = Model()
ViewObj = View()

fig = go.Figure()


app = ModelObj.DashAppObj.create_dash_app(ModelObj.DataObj.get_external_stylesheets())
ViewObj.set_layout(app)

ViewObj.set_name(app, "Multidimensional Data Visualization")


@app.callback(Output('confirm-danger', 'displayed'), Input('dropdown-danger', 'value'))
def display_confirm(value):
    if value == 'Parallel Coordinates':
        ModelObj.DataObj.set_type_of_graph('parallel_coordinates')
    elif value == 'Parallel Categories':
        ModelObj.DataObj.set_type_of_graph('parallel_categories')
    elif value == 'scatter_matrix':
        return True
    elif value == 'spidar chart':
        return True
    return False

@app.callback(Output('Mygraph', 'figure'), Input('upload-data', 'contents'), Input('upload-data', 'filename'), Input('dropdown-danger', 'value'))
def update_graph(contents, filename, value):
    if contents:
        contents = contents[0]
        filename = filename[0]
        type_of_graph = ModelObj.DataObj.get_type_of_graph()
        df = ModelObj.ResourceControllerObj.parse_data(contents, filename)
        if type_of_graph == 'parallel_coordinates':
            figure = px.parallel_coordinates(df, color = "COLOR_ID")
        elif type_of_graph == 'parallel_categories':
            figure = px.parallel_categories(df, color = "COLOR_ID")

    else:
        df = px.data.iris()
        figure = go.Figure()
    return figure

@app.callback(Output("output-data-upload", "children"), [Input("upload-data", "contents"), Input("upload-data", "filename")], )
def update_table(contents, filename):
    table = html.Div()

    if contents:
        contents = contents[0]
        filename = filename[0]
        df = ModelObj.ResourceControllerObj.parse_data(contents, filename)

        table = html.Div(
            [
                html.H5(filename),
                dash_table.DataTable(
                    data=df.to_dict("rows"),
                    columns=[{"name": i, "id": i} for i in df.columns],
                    editable=True,
                    filter_action="native",
                    sort_action="native",
                    sort_mode="multi",
                    column_selectable="single",
                    row_selectable="multi",
                    row_deletable=True,
                    selected_columns=[],
                    selected_rows=[],
                    page_action="native",
                    page_current=0,
                    page_size=25,

                ),
                html.Hr(),
                html.Div("Raw Content"),
                html.Pre(
                    contents[0:200] + "...",
                    style={"whiteSpace": "pre-wrap", "wordBreak": "break-all"},
                ),
            ]
        )

    return table

def run_server():
    app.run(debug=False, use_reloader=False)  # Turn off reloader if inside Jupyter


@app.server.route("/shutdown", methods=["POST"])
def shutdown():
    shutdown_func = request.environ.get("werkzeug.server.shutdown")
    if shutdown_func is None:
        return "Server shutdown unavailable.", 500
    shutdown_func()
    return "Server shutting down.", 200


def _pick_free_port(preferred_port=8000):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        try:
            sock.bind(("localhost", preferred_port))
            return preferred_port
        except OSError:
            sock.bind(("localhost", 0))
            return sock.getsockname()[1]


def _close_app(*_args):
    try:
        requests.post("http://127.0.0.1:8050/shutdown", timeout=1)
    except requests.RequestException:
        pass
    os._exit(0)


def eel_part():
    web_dir = Path(__file__).resolve().parent / "web"
    eel.init(str(web_dir))
    Thread(target=run_server, daemon=True).start()
    eel_port = _pick_free_port(8000)
    eel.start("main.html", host="localhost", port=eel_port, block=True, close_callback=_close_app)

class Controller:
    def _init_view(self):
        pass

