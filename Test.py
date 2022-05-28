from os import *
from os.path import *
import random

class Test:

    def __init__(self,  root_location, directory_and_files, ignored_files):
        self.directory_and_files = directory_and_files
        self.root = root_location
        self.randomized_directory_and_files = directory_and_files
        self.all_files = []
        self.ignored_files = ignored_files

    def randomize(self):
        # note this is randomizing a list that ignored some files so some are missing
        random.shuffle(self.all_files)
        iterations = 0
        for x in self.randomized_directory_and_files:
            print("\n", x[0])
            for y in x[1]:
                if isfile(join(x[0], y)):
                    random_index = random.randint(0, len(self.all_files) - 1)  # need the -1 cause we start from 0
                    # print(x[1].index(y))
                    tempIndex = x[1].index(y)
                    y = self.all_files[random_index]
                    self.randomized_directory_and_files[iterations][1][tempIndex] = y
                    del self.all_files[random_index]  # deletes item from list
            iterations += 1

        print(self.randomized_directory_and_files)

    def get_all_files(self):
        for x in self.directory_and_files:
            for y in x[1]:
                self.all_files.append(y)

        print(self.all_files)

    def index_2d(self, myList, v):
        for i, x in enumerate(myList):
            if v in x:
                return i, x.index(v)

    # def check_all_folders(self):
    #
    #     while not self.directory.isfile():
    #         print(self.directory)

    # @staticmethod  # Keep this for the finished product
    # def grab_files(startdir):
    #     filelist = ([f for f in listdir(startdir)])
    #     for x in filelist:
    #         if isfile(startdir + "\\" + x):
    #             print(x)

    # @staticmethod
    # def grab_files(startdir):
    #
    #     filelist = [f for f in listdir(startdir)]
    #     folders = []
    #     iterations = 0
    #
    #     for x in filelist:
    #
    #         if not isfile(startdir + "\\" + x):
    #             folders.append([])
    #             print(folders)
    #             folders[iterations].append(path.join(startdir + "\\" + x))
    #             iterations += 1
    #
    #     for x in filelist:
    #         if isfile(startdir + "\\" + x):
    #             folders.append(x)
    #
    #     print(folders)
    #     print(iterations)
    #
    #     for x in folders:
    #
    #         for y in listdir(x[0]):
    #
    #             x.append(y)
    #
    #         iterations -= 1
    #         if iterations == 0:
    #             break
    #
    #     print(folders)
    #     print(iterations)
