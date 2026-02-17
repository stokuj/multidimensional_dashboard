class Data:
    external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
    type_of_graph = 'parallel_coordinates'

    def get_external_stylesheets(self):
        return self.external_stylesheets

    def get_type_of_graph(self):
        return self.type_of_graph

    def set_type_of_graph(self, value):
        self.type_of_graph = value
