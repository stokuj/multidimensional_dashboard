

from controller import *
import dash


app = dash.Dash(__name__)



# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    try:
        ControllerObj = Controller()

        eel_part()
        #run_server()
        print("Run")

    except Exception as e:
        print(f"Unable to run: {e}")





