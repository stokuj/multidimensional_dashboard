# noinspection PyMethodMayBeStatic
import base64
import io
import pandas as pd

from dash import html
from dash.dependencies import Input, Output, State

class ResourceController:

    def parse_data(self, contents, filename):
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
                # df = pd.read_csv(io.StringIO(decoded.decode("utf-8")), delimiter=r"\s+")
                df = pd.read_csv(io.StringIO(decoded.decode("utf-8")), delimiter='\s+', index_col=False)
            else:
                return html.Div(["There was an error processing this file."])
        except Exception as e:
            print(e)
            return html.Div(["There was an error processing this file."])

        index = df.index
        number_of_rows = len(index)
        list = []
        for i in range(number_of_rows):
            list.append(i)

        df['COLOR_ID'] = list
        return df
