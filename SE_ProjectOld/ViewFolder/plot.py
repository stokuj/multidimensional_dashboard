import eel
import _thread

from random import randint
#from ViewFolder.dashServer import test as test
import ViewFolder.dashServer

# noinspection PyMethodMayBeStatic
class PlotWindow:
    def create_plot_window():
        try:

            ViewFolder.dashServer.eel_part()
            #ViewFolder.dashServer.run_server()
            print("test")
            #_thread.start_new_thread(ViewFolder.dashServer.eel_part())
            #_thread.start_new_thread(ViewFolder.dashServer.print_time, ("Thread-1", 2,))
            #_thread.start_new_thread(ViewFolder.dashServer.run_server())

        except:
            print("Error: unable to start thread")

        while 1:
            pass



