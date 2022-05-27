from os import *
from os.path import *


class Test:

    def __init__(self, directory, filelist):
        self.directory = directory
        self.filelist = filelist

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
