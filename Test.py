import os
import shutil
from os.path import *
import random


class Test:

    def __init__(self,  root_location, directory_and_files, ignored_files, directory_and_files_to_randomize):
        self.directory_and_files = directory_and_files
        self.root = root_location
        self.randomized_directory_and_files = directory_and_files_to_randomize
        self.all_files = []
        self.ignored_files = ignored_files

    def randomized_list(self):
        # note this is randomizing a list that ignored some files so some are missing
        random.shuffle(self.all_files)
        iterations = 0
        for x in self.randomized_directory_and_files:
            for y in x[1]:
                if isfile(join(x[0], y)):
                    random_index = random.randint(0, len(self.all_files) - 1)  # need the -1 cause we start from 0
                    # print(x[1].index(y))
                    temp_index = x[1].index(y)
                    y = self.all_files[random_index]
                    self.randomized_directory_and_files[iterations][1][temp_index] = y
                    # self.randomized_directory_and_files[iterations][1] = \
                    #     ['please.txt', 'campfire_fire.png.mcmeta', 'heheheha.txt', 'work.txt']
                    # self.randomized_directory_and_files[iterations][1][temp_index] = 'please.txt' (Hypothetical)
                    del self.all_files[random_index]  # deletes item from list
            iterations += 1

        print("Randomized List\t", self.randomized_directory_and_files)
        print("Unrandomized List\t", self.directory_and_files)

    def get_all_files(self):
        for x in self.directory_and_files:
            for y in x[1]:
                self.all_files.append(y)

    def find_rand_file(self):
        for x in self.randomized_directory_and_files:
            for y in x[1]:
                rand_file = y
                print(rand_file)
                return rand_file

    def rename_files(self):
        for x in self.directory_and_files:
            for y in x[1]:
                file = y
                directory = x[0]
                mypath = os.path.dirname(os.path.realpath(__file__))
                fullpath = (directory + "\\" + file)
                shutil.move(fullpath, mypath + "\\Temp")
                # print(mypath + "\\Temp\\" + file)

    def return_files(self):
        for x in self.randomized_directory_and_files:
            # rand_dir = x[0]
            for y in x[1]:
                file = y
                print(file)
                directory = self.find_rand_file(y)
                print(directory)
