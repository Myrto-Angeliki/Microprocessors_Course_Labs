import sys

class FileReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_circuit_file(self):
        try:
            with open(self.file_path) as f:
                lines = f.readlines()
                first_line = lines[0].split()
                return lines, first_line
        except Exception as e:
            print(f"Error {e}")
            sys.exit(2)