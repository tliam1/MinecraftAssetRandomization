import os
import shutil
# from os import *
# from os.path import *
# from RandomizerClass import Randomizer
from Test import Test


# startdir is the directory you want to start looking in, ignorelist is a list of files you want to ignore

mypath = os.path.dirname(os.path.realpath(__file__))
# print(mypath)
onlyfiles = []


def grab_files(startdir, ignorelist):

    ballslist = []

    for root, directory, files in os.walk(startdir, topdown=True):
        directory[:] = [d for d in directory if d not in ignorelist]
        files[:] = [f for f in files if f not in ignorelist]
        ballslist.append([root, files[:]])
        # print(root)
        # print(files[:])
        # print("\n" + str(ballslist))
        # print("")

    # print(ballslist)
    return ballslist


def startup():

    os.makedirs("Minecraft Randomized Textures")

    def ignore_files(directory, files):
        return [f for f in files if os.path.isfile(os.path.join(directory, f))]

    shutil.copytree(mypath + "\\TestFolder",
                    mypath + "\\Minecraft Randomized Textures\\TestFolder",
                    ignore=ignore_files)


# onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
# for f in listdir(mypath + "\\TestFolder"):
#     if isfile(join(mypath + "\\TestFolder", f)):
#         f = f.split(".")[0]
#         onlyfiles.append(f)
#         print(f)


# onlyfiles += grab_files_from_location(mypath + "\\TestFolder")
# testFolderRandomizerClass is a class that holds all the info &
# files for a specific folder. Keeps things small and organized

# test_folder_randomizer_class = Randomizer(mypath + "\\TestFolder", grab_files(mypath + "\\TestFolder"))
# test_folder_randomizer_class.randomize_file_names()  # just testing the class method
# test_folder_randomizer_class.rename_files()
# should randomize file to a temporary file name then to a minecraft file name to avoid duplicate file names

# uncomment to randomize minecraft block files

# block_texture_randomizer = Randomizer(mypath + "\\assets\\minecraft\\textures\\block",
# grab_files(mypath + "\\assets\\minecraft\\textures\\block", []))
# block_texture_randomizer.randomize_file_names()
# block_texture_randomizer.rename_files()

ignored = ["Balls.txt", "Please.txt", "kenos.txt"]

entity_texture_randomizer = Test(
                                 mypath + "\\TestFolder",
                                 grab_files(mypath + "\\TestFolder", ignored),
                                 ["Balls.txt", "Please.txt", "kenos.txt"],
                                 grab_files(mypath + "\\TestFolder", ignored)
                                )
startup()
entity_texture_randomizer.get_all_files()
entity_texture_randomizer.randomized_list()
entity_texture_randomizer.rename_and_move()  # Should now be 100% working
# entity_texture_randomizer.get_rand_file_list()  # Used for testing, turn this off when running the whole thing
# entity_texture_randomizer.get_all_files() # Also used for testing
