import os
from os import listdir
from os.path import isfile, join


mypath = 'C:\\Users\\liamk\\GrabFromFolder\\'
print(mypath)
onlyfiles = []
# onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for f in listdir(mypath):
    if isfile(join(mypath, f)):
        f = f.split(".")[0]
        onlyfiles.append(f)

print(onlyfiles)
