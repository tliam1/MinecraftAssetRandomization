import os
# from os import *
# from os.path import *
# from RandomizerClass import Randomizer
from Test import Test


# startdir is the directory you want to start looking in, ignorelist is a list of files you want to ignore

# while not grab_files_working:
#     repeatedly_bang_head_against_wall == True
#     cry()


def grab_files(startdir, ignorelist):

    ballslist = []
    allFiles = []
    for root, directory, files in os.walk(startdir, topdown=True):
        directory = [d for d in directory if d not in ignorelist]
        files = [f for f in files if f not in ignorelist]
        ballslist.append([root, files])
        # print(root)
        # print(files[:])
        # print("\n" + str(ballslist))
        # print("")

    # print(ballslist)
    return ballslist

# Old grab_files
    # filelist = [f for f in listdir(startdir)]
    # files_and_folders = []
    # iterations = 0
    #
    # for x in filelist:
    #     if not isfile(startdir + "\\" + x) and x not in ignorelist:
    #         files_and_folders.append([])
    #         files_and_folders[iterations].append(path.join(startdir + "\\" + x))
    #         iterations += 1
    #
    # for x in filelist:
    #     if isfile(startdir + "\\" + x) and x not in ignorelist:
    #         files_and_folders.append(x)
    #
    # print(files_and_folders)
    # print(iterations)
    #
    # for x in files_and_folders:  # Grabs files from inside of the folders that are found
    #     if iterations == 0:
    #         break
    #     for y in listdir(x[0]):
    #         if y not in ignorelist:
    #             x.append(y)
    #     iterations -= 1
    #
    # print(files_and_folders)
    # print(iterations)
    # return files_and_folders


mypath = os.path.dirname(os.path.realpath(__file__))
# print(mypath)
onlyfiles = []

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
# test_folder_randomizer_class.rename_files()  # should randomize file to a temporary file name then to a minecraft file name to avoid duplicate file names

# uncomment to randomize minecraft block files

# block_texture_randomizer = Randomizer(mypath + "\\assets\\minecraft\\textures\\block", grab_files(mypath + "\\assets\\minecraft\\textures\\block", []))
# block_texture_randomizer.randomize_file_names()
# block_texture_randomizer.rename_files()

entity_texture_randomizer = Test(mypath + "\\TestFolder", grab_files(mypath + "\\TestFolder", ["Balls.txt", "Please.txt", "kenos.txt"]), ["Balls.txt", "Please.txt", "kenos.txt"])
entity_texture_randomizer.get_all_files()
entity_texture_randomizer.randomize()


# Below just takes testFolderRandomizerClass.files and adds it to a file in randomizer_name_storage,
# I don't really know how to orgnaize all of this yet really, so it is stil to be determined if I'm just going
# to put this into a function, put it in a class, etc.
# Also, for now it is taking the file names from TestFolder.

# def store_file_names():
#     testfile = open(mypath + "\\randomizer_name_storage" + "\\TestFile.txt", "w")
#
#     for file in test_folder_randomizer_class.files:
#         testfile.write(file + "\n")
