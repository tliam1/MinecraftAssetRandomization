class randomizer:
    def __init__(self, directory, files):
        self.directory = directory
        self.files = files

    def randomizeFileNames(self):
        # randomize list and make if's for exclusions
        print("Testing function", self.files)
