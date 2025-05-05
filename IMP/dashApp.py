import dash

class DashApp:
    def create_dash_app(self, external_stylesheets):

        app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
        return app

    def run(self,app):
        app.run(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter