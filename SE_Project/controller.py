from model import Model
from view import View

import plotly.graph_objects as go
import plotly.express as px
from dash import html
from dash import dash_table
import eel
from dash.dependencies import Input, Output, State
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


def eel_part():
    eel.init('web')

    def my_other_thread():
        eel.sleep(5.0)  # Use eel.sleep(), not time.sleep()

    eel.spawn(my_other_thread)

    eel.start('main.html', block=False)  # Don't block on this call

    eel.sleep(2.0)
    run_server()

    while True:
        eel.sleep(5.0)  # Use eel.sleep(), not time.sleep()





class Controller:
    def _init_view(self):
        pass

