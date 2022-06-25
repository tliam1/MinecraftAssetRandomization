import os
import shutil
from os.path import *
import random


class Randomizer:

    def __init__(self,  root_location, directory_and_files, ignored_files, directory_and_files_to_randomize, same_list):
        self.directory_and_files = directory_and_files
        self.root = root_location
        self.randomized_directory_and_files = directory_and_files_to_randomize
        self.all_files = []
        self.ignored_files = ignored_files
        self.same_list = same_list

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

        # print("Randomized List\t", self.randomized_directory_and_files)
        # print("Unrandomized List\t", self.directory_and_files)

    def get_all_files(self):
        for x in self.directory_and_files:
            for y in x[1]:
                self.all_files.append(y)

    def find_dir(self, rand_file, mc_ver):
        iterations = 0
        for x in self.directory_and_files:
            directory = x[0]
            for y in x[1]:
                if rand_file == y:
                    temp_index = self.directory_and_files[iterations][1].index(y)

                    directory = directory.replace("assets",
                                                  "Randomized_MC_Assets\\Minecraft "
                                                  + mc_ver +
                                                  " Randomized Textures\\assets")
                    del self.directory_and_files[iterations][1][temp_index]
                    return directory
            iterations += 1

    def get_rand_file_list(self):
        rand_file_list = []
        for x in self.randomized_directory_and_files:
            for y in x[1]:
                rand_file_list.append(y)
                # print(rand_file_list)
        return rand_file_list

    def rename_and_move(self, mc_ver):
        rand_file_list = self.get_rand_file_list()
        iteration = 0
        using_python = False
        if using_python:
            mypath = os.path.dirname(os.path.realpath(__file__))
        else:
            mypath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "app"

        logfile = open(mypath + "/Randomized_MC_Assets/Minecraft " + mc_ver + " Randomized Textures/log.txt", "a")
        for x in self.same_list:
            for y in x[1]:
                file = y
                directory = x[0]
                print(directory)
                fullpath = (directory + "/" + file)
                print(fullpath)
                # shutil.copy(fullpath, mypath + "/Temp")
                print("CP 4.5")
                print(shutil.copy(fullpath, mypath + "/Temp/"))
                print(os.listdir(mypath+"/Temp/"))
                print("CP5")
                if os.path.exists(mypath + "/Temp"):
                    print("Temp file exists here!")
                if os.path.exists(directory):
                    print("directory exists")
                if os.path.exists(fullpath):
                    print("full path exists")
                if os.path.exists(mypath + "/Temp/" + file):
                    print("File Exists in Temp folder")
                os.rename(mypath + "/Temp/" + file, os.path.join(mypath + "/Temp/", rand_file_list[iteration]))
                print("CP5.5f")
                new_directory = self.find_dir(rand_file_list[iteration], mc_ver)
                print("CP6")
                shutil.move(mypath + "/Temp/" + rand_file_list[iteration], new_directory)
                print("CP7")
                logfile.write(rand_file_list[iteration] + " is " + file + "\n")

                iteration += 1
                # print("Randomized " + str(iteration) + " file(s)")
        else:
            logfile.close()


