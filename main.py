import os
from os import listdir
from os.path import isfile, join
from RandomizerClass import randomizer


def grab_files_from_location(directoryname):
    fileslist = [f for f in listdir(directoryname) if isfile(join(directoryname, f))]
    return fileslist


mypath = os.path.dirname(os.path.realpath(__file__))
print(mypath)
onlyfiles = []

# onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
# for f in listdir(mypath + "\\TestFolder"):
#     if isfile(join(mypath + "\\TestFolder", f)):
#         f = f.split(".")[0]
#         onlyfiles.append(f)
#         print(f)


# onlyfiles += grab_files_from_location(mypath + "\\TestFolder")
# testFolderRandomizerClass is a class that holds all the info & files for a specific folder. Keeps things small and organized
testFolderRandomizerClass = randomizer(mypath + "\\TestFolder", grab_files_from_location(mypath + "\\TestFolder"))
print(testFolderRandomizerClass.files)
testFolderRandomizerClass.randomizeFileNames()  # just testing the class method


