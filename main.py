import os
from os.path import exists
import shutil
import time
from queue import *

from RandomizerScript import Randomizer

# This specifies when things can be randomized, dont delelte this
q = Queue()
can_randomize = True
# This is the full ignored list, don't delete this
ignored_textures_default = ["advancements", "container", "presets", "title", "colormap", "effect", "texts",
                            "accessibility.png", "bars.png", "checkbox.png", "icons.png", "recipe_book.png",
                            "recipe_button.png", "resource_packs.png", "server_selection.png",
                            "social_interactions.png", "spectator_widgets.png", "stream_indicator.png", "toasts.png",
                            "widgets.png", "world_selection.png", "rain.png", "snow.png", "end_sky.png", "clouds.png",
                            "map_icons.png", "nausea.png", "powder_snow_outline.png", "pumpkinblur.png", "shadow.png",
                            "spyglass_scope.png", "underwater.png", "unknown_pack.png", "unknown_server.png",
                            "vignette.png", "white.png", ".gitignore", "gpu_warnlist.json",
                            "regional_compliancies.json", "pack.png"]

ignored_music_default = ["ambient", "block", "damage", "dig", "enchant", "entity", "event", "fire", "fireworks", "item",
                         "liquid", "minecart", "mob", "note", "portal", "random", "step", "tile", "ui"]

ignored_sounds_default = ["music", "records"]
using_python = False

if using_python:
    mypath = os.path.dirname(os.path.abspath(__file__))
else:
    mypath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "app"


# print(mypath)

# startdir is the directory you want to start looking in, ignorelist is a list of files you want to ignore


def grab_files(startdir, ignorelist):
    ballslist = []

    for root, directory, files in os.walk(startdir, topdown=True):
        directory[:] = [d for d in directory if d not in ignorelist]
        files[:] = [f for f in files if f not in ignorelist and not f.endswith(".mcmeta")]
        ballslist.append([root, files[:]])

    return ballslist


# preps zip file then deletes source, and sets download timer

def zip_files(destination, source):
    if exists(destination):
        print("OMG WE FUCKING DID IT")
    shutil.make_archive(destination + "/Randomized_MC_Assets", 'zip', source)  # creates zip
    shutil.rmtree(source)  # removes the Randomized MC folder
    # current_time = time.time()  # sets current time
    # while abs(current_time - time.time()) < 1:  # this is the time before auto removes download (5 sec)
    #     continue
    # print("Open Randomizations")
    q.queue.clear()
    list_of_globals = globals()
    list_of_globals["can_randomize"] = True


def can_download():
    return can_randomize


def halt_download():
    current_time = time.time()  # sets current time
    while abs(current_time - time.time()) < 5:  # this is the time before auto removes download (5 sec)
        # we just need the download to basically start then we are good
        # 5 seconds for good measure
        continue
    return True


def try_download():  # if someone is in the process of downloading, wait
    try:
        if exists(mypath + "/static/zipFiles/Randomized_MC_Assets.zip"):
            os.remove(mypath + "/static/zipFiles/Randomized_MC_Assets.zip")  # removes zip from folder
    except PermissionError:
        return False
    return True


def try_create():  # if someone is in the process of downloading, wait
    try:
        os.makedirs("Randomized_MC_Assets")
    except FileExistsError:
        return False
    return True


def randomize(mc_ver, ignored_textures, ignored_music, ignored_sounds, bypass):
    print(mypath)
    if not bypass:
        halt_download()
    if not can_download():
        print("we cannot download rn")
        return

    list_of_globals = globals()
    list_of_globals["can_randomize"] = False

    if not try_download():
        print("NO EXE EXISTS SO WE WILL WAIT FOR A RANDOMIZATION PROCESS")
        return
    # if not try_download():  # if removing the zip folder causes a permissions error...wait
    #     return
    # if not try_create(mc_ver):
    #     return

    vers_to_mcmeta = {"1.19": "9"}
    if not try_create():
        print("got stuck & process is broken")
        return
    os.makedirs(mypath+"/Randomized_MC_Assets/Minecraft " + mc_ver + " Randomized Textures")
    # os.makedirs("Randomized_MC_Assets")
    # shutil.move(mypath + "/Randomized_MC_Assets/Minecraft " + mc_ver + " Randomized Textures", mypath + "/Randomized_MC_Assets")

    def ignore_files(directory, files):
        return [f for f in files if os.path.isfile(os.path.join(directory, f))]

    shutil.copytree(mypath + "/assets",
                    mypath + "/Randomized_MC_Assets/Minecraft " + mc_ver + " Randomized Textures/assets",
                    ignore=ignore_files)

    shutil.copy(mypath + "/Copyables/pack.png",
                mypath + "/Randomized_MC_Assets/Minecraft " + mc_ver + " Randomized Textures")

    shutil.copy(mypath + "/Copyables/end.txt",
                mypath + "/Randomized_MC_Assets/Minecraft " + mc_ver +
                " Randomized Textures/assets/minecraft/texts")

    shutil.copy(mypath + "/Copyables/splashes.txt",
                mypath + "/Randomized_MC_Assets/Minecraft " + mc_ver +
                " Randomized Textures/assets/minecraft/texts")

    mcmeta = open(mypath + "/Randomized_MC_Assets/Minecraft " + mc_ver + " Randomized Textures/pack.mcmeta", "a")

    mcmeta.write("{\n \"pack\": {\n   \"pack_format\": " + vers_to_mcmeta[mc_ver] + ",\n   "
                 "\"description\": \"Minecraft textures randomized by Izokia and CosmicShiny\"\n }\n}")
    mcmeta.close()

    logfile = open(mypath + "/Randomized_MC_Assets/Minecraft " + mc_ver + " Randomized Textures/log.txt", "a")
    logfile.write("Format: (File_name) is (File_image)\n\n")
    logfile.close()
    print("\nRandomizing textures\n")
    texture_randomzier = Randomizer(
        mypath + "/assets",
        grab_files(mypath + "/assets/minecraft/textures", ignored_textures),
        [],
        grab_files(mypath + "/assets/minecraft/textures", ignored_textures),
        grab_files(mypath + "/assets/minecraft/textures", ignored_textures)
    )
    texture_randomzier.get_all_files()
    texture_randomzier.randomized_list()
    texture_randomzier.rename_and_move(mc_ver)
    print("\nTextures have finished randomizing\n")

    # print("\nRandomizing music\n")
    # songs_randomizer = Randomizer(
    #         mypath + "\\assets",
    #         grab_files(mypath + "\\assets\\minecraft\\sounds", ignored_music),
    #         [],
    #         grab_files(mypath + "\\assets\\minecraft\\sounds", ignored_music)
    #         )
    # songs_randomizer.get_all_files()
    # songs_randomizer.randomized_list()
    # songs_randomizer.rename_and_move(mc_ver)
    # print("\nMusic has finished randomizing\n")

    print("\nRandomizing sounds\n")
    songs_randomizer = Randomizer(
        mypath + "/assets",
        grab_files(mypath + "/assets/minecraft/sounds", ignored_sounds),
        [],
        grab_files(mypath + "/assets/minecraft/sounds", ignored_sounds),
        grab_files(mypath + "/assets/minecraft/sounds", ignored_sounds)
    )
    songs_randomizer.get_all_files()
    songs_randomizer.randomized_list()
    songs_randomizer.rename_and_move(mc_ver)
    print("\nSounds have finished randomizing\n")
    print("Files have finished randomizing")
    # You can comment zip_files out if you just want to randomize for yourself, but it doesn't really change anything
    # other than not zipping the end result
    if not bypass:
        zip_files(mypath + "/static/zipFiles", mypath + "/Randomized_MC_Assets")


# run this once to start the program
# randomize("1.19", ignored_textures_default, ignored_music_default, ignored_sounds_default, True)
