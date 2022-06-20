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

    def find_dir(self, rand_file):
        for x in self.directory_and_files:
            directory = x[0]
            for y in x[1]:
                if rand_file == y:
                    directory = directory.replace("TestFolder", "Minecraft Randomized Textures\\TestFolder")
                    return directory + "\\" + rand_file

    def get_rand_file_list(self):
        rand_file_list = []
        for x in self.randomized_directory_and_files:
            for y in x[1]:
                rand_file_list.append(y)
                # print(rand_file_list)
        return rand_file_list

    def rename_and_move(self):
        rand_file_list = self.get_rand_file_list()
        iteration = 0
        mypath = os.path.dirname(os.path.realpath(__file__))
        for x in self.directory_and_files:
            for y in x[1]:
                file = y
                directory = x[0]
                fullpath = (directory + "\\" + file)
                shutil.copy(fullpath, mypath + "\\Temp")
                os.rename(mypath + "\\Temp\\" + file, mypath + "\\Temp\\" + rand_file_list[iteration])
                new_directory = self.find_dir(rand_file_list[iteration])
                shutil.move(mypath + "\\Temp\\" + rand_file_list[iteration], new_directory)
                iteration += 1
                print("Randomized " + str(iteration) + " file(s)")
        else:
            print("\nRandomization Finished. Randomization list can be found in log.txt in texture pack folder")
            logfile = open(mypath + "\\Minecraft Randomized Textures\\log.txt", "a")
            logfile.write("Randomized List:\n" + str(self.randomized_directory_and_files) + "\n")
            logfile.write("Unrandomized List:\n" + str(self.directory_and_files))
