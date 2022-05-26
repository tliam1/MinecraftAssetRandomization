import os
from os import listdir
from os.path import isfile, join
import random

class Randomizer:
    def __init__(self, directory, files):  # I included the directory so we dont have to keep stating it
        self.directory = directory
        self.files = files
        # print(self.files)

    def randomize_file_names(self):
        # randomize list and make if's for exclusions
        random.shuffle(self.files)
        # print("Testing function", self.files)

    def rename_files(self):  # we need to give a temp name so that we dont create files with the same name
        iterations = 0
        for f in listdir(self.directory):  # first we set the file name to a sample number because we can't have two file names
            if isfile(join(self.directory, f)) and not f.split("y")[0] == "z" and not f.endswith(".mcmeta"):  # check if it is a file and does not have name starting with z before the first y (Not a temp file name)
                # ignore minecraft MetaFiles
                # print(f)
                # okay really bad, but we change have the file order change so adding zzzz's make sure all the new files get pushed back and order never changes
                # as the files order is alphabetical then #'s 0-9
                os.rename(self.directory + "\\" + f, self.directory + f"\\zyzzz{iterations}.txt")  # the brackets allow us to use ints in a string (using a + or comma breaks the funtion)
                iterations += 1
        print(self.files)
        iterations = 0
        for f in listdir(self.directory):  # now we can rename all files with the random names without errors of two files with the same name
            while self.files[iterations].endswith(".mcmeta"):
                iterations += 1  # while we are on a file that isnt allowed we add to our iteration count
            if isfile(join(self.directory, f)) and f.split("y")[0] == "z" and iterations < len(self.files) and not self.files[iterations].endswith(".mcmeta"):
                # If there are any files not starting with z before the first y we ignore it
                # no changing files with .mcmeta
                os.rename(self.directory + "\\" + f, self.directory + "\\" + self.files[iterations])
                iterations += 1

