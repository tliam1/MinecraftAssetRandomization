import os
import shutil
# from os import *
# from os.path import *
# from RandomizerClass import Randomizer
from RandomizerScript import Randomizer

# startdir is the directory you want to start looking in, ignorelist is a list of files you want to ignore

mypath = os.path.dirname(os.path.realpath(__file__))
# print(mypath)


def grab_files(startdir, ignorelist):

    ballslist = []

    for root, directory, files in os.walk(startdir, topdown=True):
        directory[:] = [d for d in directory if d not in ignorelist]
        files[:] = [f for f in files if f not in ignorelist and not f.endswith(".mcmeta")]
        ballslist.append([root, files[:]])

    return ballslist


def startup():

    os.makedirs("Minecraft Randomized Textures")

    def ignore_files(directory, files):
        return [f for f in files if os.path.isfile(os.path.join(directory, f))]

    shutil.copytree(mypath + "\\assets",
                    mypath + "\\Minecraft Randomized Textures\\assets",
                    ignore=ignore_files)

    shutil.copy(mypath + "\\Copyables\\pack.mcmeta",
                mypath + "\\Minecraft Randomized Textures")

    shutil.copy(mypath + "\\Copyables\\pack.png",
                mypath + "\\Minecraft Randomized Textures")

    shutil.copy(mypath + "\\Copyables\\end.txt",
                mypath + "\\Minecraft Randomized Textures\\assets\\minecraft\\texts")

    shutil.copy(mypath + "\\Copyables\\splashes.txt",
                mypath + "\\Minecraft Randomized Textures\\assets\\minecraft\\texts")


ignored = ["advancements", "container", "presets", "title", "colormap", "effect", "texts", "accessibility.png",
           "bars.png", "checkbox.png", "icons.png", "recipe_book.png", "recipe_button.png", "resource_packs.png",
           "server_selection.png", "social_interactions.png", "spectator_widgets.png", "stream_indicator.png",
           "toasts.png", "widgets.png", "world_selection.png" "rain.png", "snow.png", "end_sky.png", "clouds.png",
           "map_icons.png", "nausea.png", "powder_snow_outline.png", "pumpkinblur.png", "shadow.png",
           "spyglass_scope.png", "underwater.png", "unknown_pack.png", "unknown_server.png", "vignette.png",
           "white.png", ".gitignore", "gpu_warnlist.json", "regional_compliancies.json"]

entity_texture_randomizer = Randomizer(
                                 mypath + "\\assets",
                                 grab_files(mypath + "\\assets", ignored),
                                 [],
                                 grab_files(mypath + "\\assets", ignored)
                                )


def start_program():
    startup()
    entity_texture_randomizer.get_all_files()
    entity_texture_randomizer.randomized_list()
    entity_texture_randomizer.rename_and_move()  # Should now be 100% working

# Careful when using code below, check to make sure it isn't going to fuck with anything, would recommend
# turning rename_and_move() off first

# entity_texture_randomizer.get_rand_file_list()  # Used for testing, turn this off when running the whole thing
# entity_texture_randomizer.get_all_files() # Also used for testing
