class MyOpen:
    def __init__(self, file):
        self.file = file

    def __enter__(self):
        try:
            self.file_er = open(self.file)
        except IOError:
            self.file_er = open(self.file, "w")
        self.file_er = open(self.file, "r")
        return self.file_er

    def __exit__(self, exp_type, exp_value, traceback):
        self.file_er.close()


