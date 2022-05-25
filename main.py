import os
from os import listdir
from os.path import isfile, join

def grabFilesFromLocation(directoryName):
    print(directoryName)


mypath = os.path.dirname(os.path.realpath(__file__))
print(mypath)
onlyfiles = []
# onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for f in listdir(mypath):
    if isfile(join(mypath, f)):
        f = f.split(".")[0]
        onlyfiles.append(f)

#mypath = grabFilesFromLocation()
print(onlyfiles)
print("Balls")

print("Balls")
