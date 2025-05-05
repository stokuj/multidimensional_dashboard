import plotly.graph_objects as go # or plotly.express as px
import plotly.express as px
import base64
import cufflinks as cf
import base64
import datetime
import io
import pandas as pd
import time
import eel
from dash.dependencies import Input, Output, State
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import dash_bootstrap_components as dbc
from dash import html
fig = go.Figure() # or any Plotly Express function e.g. px.bar(...)
# fig.add_trace( ... )
# fig.update_layout( ... )


available_indicators = ['test1', 'test2', 'test3','test4','test5','test6']

x = 0

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div([
    dcc.Upload(
        id="upload-data",
        children=html.Div(["Drag and Drop or ", html.A("Select Files")]),
        style={
            "width": "100%",
            "height": "60px",
            "lineHeight": "60px",
            "borderWidth": "1px",
            "borderStyle": "dashed",
            "borderRadius": "5px",
            "textAlign": "center",
            "margin": "10px",
        },
        # Allow multiple files to be uploaded
        multiple=True,
    ),
    dcc.ConfirmDialog(
        id='confirm-danger',
        message='Danger danger! Are you sure you want to continue?',
    ),

    dcc.Dropdown(
        options=[
            {'label': i, 'value': i}
            for i in ['Parallel Coordinates', 'scatter_matrix', 'spider chart']
        ],
        value='Parallel Coordinates',
        id='dropdown-danger'
    ),
    html.Hr(),
    html.H1('Select graph color:'),
    dcc.RadioItems(
        id='crossfilter-xaxis-type',
        options=[{'label': i, 'value': i} for i in ['Red', 'Blue']],
        value='Linear',
        labelStyle={'display': 'inline-block'}
    ),
    html.Hr(),
    dcc.Dropdown(
        options=[
            {'label': i, 'value': i}
            for i in available_indicators
        ],
        id='dropdown-test',
    ),
    dcc.ConfirmDialog(
        id='confirm-test',
        message='Danger danger! Are you sure you want to continue?',
    ),
    dcc.Graph(id="Mygraph"),
    html.Div(id="output-data-upload"),
])




@app.callback(Output('confirm-test', 'displayed'), Input('dropdown-test', 'value'))
def display_confirm(value):
    if value == 'test1':
        set(1)
        return True
    elif value == 'test2':
        set(2)
        return True
    elif value == 'test3':
        set(3)
        return True
    elif value == 'test4':
        set(4)
        return True
    elif value == 'test5':
        set(5)
        return True
    elif value == 'test6':
        set(6)
        return True
    return False


@app.callback(Output('confirm-danger', 'displayed'), Input('dropdown-danger', 'value'))
def display_confirm(value):
    if value == 'scatter_matrix':
        return True
    elif value == 'spidar chart':
        return True
    return False


@app.callback(
        Output('Mygraph', 'figure'),

            Input('upload-data', 'contents'), Input('upload-data', 'filename'),
            Input('dropdown-test', 'value'), Input('dropdown-test', 'value'),
    )
def update_graph(contents, filename, tmp1, tmp2):
    if contents:
        contents = contents[0]
        filename = filename[0]
        df = parse_data(contents, filename)
        print('test')
        print(x)
        figure = px.parallel_coordinates(df, color=df.columns[0+x])
    else:
        df = px.data.iris()
        figure = go.Figure()
    return figure

def parse_data(contents, filename):
    content_type, content_string = contents.split(",")

    decoded = base64.b64decode(content_string)
    try:
        if "csv" in filename:
            # Assume that the user uploaded a CSV or TXT file
            df = pd.read_csv(io.StringIO(decoded.decode("utf-8")))
        elif "xls" in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
        elif "txt" or "tsv" in filename:
            # Assume that the user upl, delimiter = r'\s+'oaded an excel file
            #df = pd.read_csv(io.StringIO(decoded.decode("utf-8")), delimiter=r"\s+")
            df = pd.read_csv(io.StringIO(decoded.decode("utf-8")), delimiter='\s+', index_col=False)
        else:
            return html.Div(["There was an error processing this file."])
    except Exception as e:
        print(e)
        return html.Div(["There was an error processing this file."])

    return df


@app.callback(Output("output-data-upload", "children"),[Input("upload-data", "contents"), Input("upload-data", "filename")],)
def update_table(contents, filename):
    table = html.Div()

    if contents:
        contents = contents[0]
        filename = filename[0]
        df = parse_data(contents, filename)

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
                    page_current= 0,
                    page_size= 25,

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
    app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter
    
def print_time(threadName, delay):
        count = 0
        while count < 5:
            time.sleep(delay)
            count += 1
            print("%s: %s" % (threadName, time.ctime(time.time())))
            
def eel_part():
    eel.init('web')

    def my_other_thread():
        pass
            #eel.sleep(5.0)  # Use eel.sleep(), not time.sleep()

    eel.spawn(my_other_thread)

    eel.start('test.html', block=False)  # Don't block on this call

    eel.sleep(1.0)  # minimalna warosc
    run_server()
    while True:
        eel.sleep(5.0)  # Use eel.sleep(), not time.sleep()

def set(value):
    global x
    x = value
    print(x)
