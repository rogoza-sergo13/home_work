class MyOpen:
    def __init__(self, file, mode):
        self.file = file
        self.mode = mode

    def __enter__(self):
        self.file = open(self.file, self.mode)
        return self.file

    def __exit__(self, exp_type, exp_value, traceback):
        self.file.close()
