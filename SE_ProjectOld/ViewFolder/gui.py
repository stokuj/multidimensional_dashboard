from ViewFolder.plot import PlotWindow as Plo

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import threading
import time
import webbrowser


# noinspection PyMethodMayBeStatic
class GUI:
    def create_main_window():
        # Let's create the Tkinter window
        main_window = Tk()
        main_window.title("myGUI")
        main_window.geometry("250x250")

        # EmptyBOX
        # tkinter.Label(window, text="Path to your file").grid(row=0)
        # tkinter.Entry(window).grid(row=0, column=1)

        #Checkbutton(main_window, text="Keep Me Logged In").grid(columnspan=2)
        #Checkbutton(main_window, text=".txt").grid(columnspan=3)

        def myGUI_helper_button_pressed():
            helper_window = Tk()
            helper_window.title("myGUI")
            helper_window.geometry("300x50")
            Label(helper_window, text="Select your configuration and click button START").grid(columnspan=1)
            helper_window.mainloop()

        Button(main_window, text="myGUI Helper", command=myGUI_helper_button_pressed).grid(row = 0, column = 0, sticky = W, pady = 2)

        def error_button_pressed():
             messagebox.showerror('Python Error', 'Error: This is an Error Message!')

        Button(main_window, text="Error Button", command=error_button_pressed).grid(columnspan=1, column=1)

        def import_file_button_pressed():
            filepath = filedialog.askopenfilename(initialdir="C:\\",
                                                  title="Import file",
                                                  filetypes=(("text files", "*.txt"),
                                                             ("all files", "*.*")))
            file = open(filepath, 'r')
            print(file.read())
            file.close()
            # return structure to controller

        Button(main_window, text="Select Input", command=import_file_button_pressed).grid(columnspan=1, column=1)

        def HTML_button_pressed():
            #t0 = threading.Thread(target=test_f)
            #t1 = threading.Thread(target=Plo.create_plot_window)
            #t1.start()
            #t1.join()
            #t0.start()
            #t0.join()
            webbrowser.open('plot.html', new=2)

        Button(main_window, text="OPEN IN WEB", command=HTML_button_pressed).grid(columnspan=1)

        main_window.mainloop()

    def create_main_window2():
        Plo.create_plot_window()
