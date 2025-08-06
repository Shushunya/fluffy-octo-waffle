# TODO: try to use logger
class FileLogger:
    def __init__(self, path="logs.txt"):
        self.path = path
        self.log_file = None

    def __enter__(self):
        self.log_file = open(self.path, "a")
        return self.log_file


    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.log_file and self.log_file.closed:
            self.log_file.close()
