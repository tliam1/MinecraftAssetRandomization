
class Randomizer:

    def __init__(self, directory, files):  # I included the directory so we dont have to keep stating it
        self.directory = directory
        self.files = files

    def randomize_file_names(self):
        # randomize list and make if's for exclusions
        print("Testing function", self.files)
