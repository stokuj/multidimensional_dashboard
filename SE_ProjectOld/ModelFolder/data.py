class Data:
    inputFileName = "test2"
    outputFileName = ""
    multi_dimensional_data = any
    number_of_features = 0
    index = 0

    def set_input_file_name(self, name):
        self.inputFileName = name

    def set_output_file_name(self, name):
        self.outputFileName = name

    def get_input_file_name(self):
        return self.inputFileName

    def get_output_file_name(self):
        return self.outputFileName
