from model import Model
from view import View
from ControllerFolder.dataCorrection import DataCorrection
from ControllerFolder.resourceController import ResourceController


# noinspection PyMethodMayBeStatic
class Controller:
    DataCorrection = DataCorrection
    ResourceController = ResourceController

    def _init(self):
        self.model = Model(self)
        self.view = View(self)

    def run(self):

        View.GUI.create_main_window2()
        #View.GUI.create_main_window()
        #View.print_basic_info()
        
        #Model.Data.set_input_file_name(Model.Data, View.take_string_from_user())
        
        #View.print_custom_msg("Hello " + Model.Data.get_input_file_name(Model.Data))

