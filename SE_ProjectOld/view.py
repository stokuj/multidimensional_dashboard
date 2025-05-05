from ViewFolder.gui import GUI


# noinspection PyMethodMayBeStatic
class View:
    GUI = GUI

    def _init_view(self, controller):
        self.controller = controller

    def print_custom_msg(str):
        print(str)

    @classmethod
    def print_basic_info(cls):
        print("Hello World")
        print("Enter your name: ")

    @classmethod
    def take_string_from_user(cls):
        tmp = input()
        return tmp

    def export_graph():
        pass
    
    def read_user_settings(self):
        pass



