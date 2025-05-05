# noinspection PyMethodMayBeStatic

from resourceController import ResourceController
from data import Data
from dashApp import DashApp
from resourceController import  ResourceController

class Model:
    DashAppObj = DashApp()
    DataObj = Data()
    ResourceControllerObj = ResourceController()

    def _init_view(self, controller):
        self.controller = controller

    def set(self, value):
        global x
        x = value
        print(x)


