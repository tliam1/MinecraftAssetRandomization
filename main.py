import os
from os import listdir
from os.path import isfile, join


def grab_files_from_location(directoryname):
    fileslist = [f for f in listdir(directoryname) if isfile(join(directoryname, f))]
    return fileslist


mypath = os.path.dirname(os.path.realpath(__file__))
print("piss")
onlyfiles = []

# onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
# for f in listdir(mypath + "\\TestFolder"):
#     if isfile(join(mypath + "\\TestFolder", f)):
#         f = f.split(".")[0]
#         onlyfiles.append(f)
#         print(f)


onlyfiles += grab_files_from_location(mypath + "\\TestFolder")

print(onlyfiles)

print("I love bofa")
print("bofa these nuts")
print("heheha grr")