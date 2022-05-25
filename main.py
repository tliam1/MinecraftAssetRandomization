import os
from os import listdir
from os.path import isfile, join


def grab_files_from_location(directoryname):
    filesList = [f for f in listdir(directoryname) if isfile(join(directoryname, f))]
    return filesList


mypath = os.path.dirname(os.path.realpath(__file__))
print(mypath)
onlyfiles = []

# onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
# for f in listdir(mypath + "\\TestFolder"):
#     if isfile(join(mypath + "\\TestFolder", f)):
#         f = f.split(".")[0]
#         onlyfiles.append(f)
#         print(f)


onlyfiles += grab_files_from_location(mypath + "\\TestFolder")

print(onlyfiles)