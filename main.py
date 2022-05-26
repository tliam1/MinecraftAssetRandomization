import os
from os import listdir
from os.path import isfile, join
from RandomizerClass import Randomizer


def grab_files_from_location(directoryname):
    fileslist = [f for f in listdir(directoryname) if isfile(join(directoryname, f))]
    return fileslist


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
test_folder_randomizer_class = Randomizer(mypath + "\\TestFolder", grab_files_from_location(mypath + "\\TestFolder"))
test_folder_randomizer_class.randomize_file_names()  # just testing the class method
test_folder_randomizer_class.rename_files()  # should randomize file to a temperary file name then to a minecraft file name to avoid duplicate file names

# uncomment to randomize minecraft block files
# block_texture_randomizer = Randomizer(mypath + "\\assets\\minecraft\\textures\\block", grab_files_from_location(mypath + "\\assets\\minecraft\\textures\\block"))
# block_texture_randomizer.randomize_file_names()
# block_texture_randomizer.rename_files()


# Below just takes testFolderRandomizerClass.files and adds it to a file in randomizer_name_storage,
# I don't really know how to orgnaize all of this yet really, so it is stil to be determined if I'm just going
# to put this into a function, put it in a class, etc.
# Also, for now it is taking the file names from TestFolder.


def store_file_names():
    testfile = open(mypath + "\\randomizer_name_storage" + "\\TestFile.txt", "w")

    for file in test_folder_randomizer_class.files:
        testfile.write(file + "\n")
