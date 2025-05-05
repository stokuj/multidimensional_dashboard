# noinspection PyMethodMayBeStatic

from ModelFolder.graph import Graph
from ModelFolder.data import Data


class Model:
    Graph = Graph
    Data = Data


    def _init_model(self, controller):
        self.controller = controller
        #self.graph = Graph(self)
        #self.data = Data(self)

    def check_input(self):
        pass

    def draw_graph(self):
        pass
