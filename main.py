from app.controller import Controller, eel_part


if __name__ == "__main__":
    try:
        ControllerObj = Controller()
        eel_part()
        print("Run")
    except Exception as e:
        print(f"Unable to run: {e}")
