import os
from os.path import exists
import shutil
import time

from RandomizerScript import Randomizer

# This specifies when things can be randomized, dont delelte this
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

mypath = os.path.dirname(os.path.realpath(__file__))

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
def zip_and_delete(destination, source):
    shutil.make_archive(destination + "/Randomized_MC_Assets", 'zip', source)  # creates zip
    shutil.rmtree(source)  # removes the Randomized MC folder
    current_time = time.time()  # sets current time
    while abs(current_time - time.time()) < 1:  # this is the time before auto removes download (5 sec)
        continue
    list_of_globals = globals()
    list_of_globals['can_randomize'] = True  # allow future randomizations again
    print("Open Randomizations")

def halt_download():
    current_time = time.time()  # sets current time
    while abs(current_time - time.time()) < 3:  # this is the time before auto removes download (5 sec)
        continue
    return True

def try_download():  # if someone is in the process of downloading, wait
    try:
        if exists(mypath + "/static/zipFiles/Randomized_MC_Assets.zip"):
            os.remove(mypath + "/static/zipFiles/Randomized_MC_Assets.zip")  # removes zip from folder
    except PermissionError:
        return False
    return True

def randomize(mc_ver, ignored_textures, ignored_music, ignored_sounds):

    list_of_globals = globals()
    list_of_globals['can_randomize'] = False  # stop all future randomizations
    while not try_download():  # if someone is in the process of downloading, wait
        continue
    os.makedirs("Minecraft " + mc_ver + " Randomized Textures")

    def ignore_files(directory, files):
        return [f for f in files if os.path.isfile(os.path.join(directory, f))]

    shutil.copytree(mypath + "\\assets",
                    mypath + "\\Minecraft " + mc_ver + " Randomized Textures\\assets",
                    ignore=ignore_files)
    shutil.copy(mypath + "\\Copyables\\pack.png",
                mypath + "\\Minecraft " + mc_ver + " Randomized Textures")
    shutil.copy(mypath + "\\Copyables\\end.txt",
                mypath + "\\Minecraft " + mc_ver + " Randomized Textures\\assets\\minecraft\\texts")
    shutil.copy(mypath + "\\Copyables\\splashes.txt",
                mypath + "\\Minecraft " + mc_ver + " Randomized Textures\\assets\\minecraft\\texts")
    mcmeta = open(mypath + "\\Minecraft " + mc_ver + " Randomized Textures\\pack.mcmeta", "a")
    mcmeta.write("{\n \"pack\": {\n   \"pack_format\": 9,\n   "
                 "\"description\": \"Minecraft textures randomized by Izokia and CosmicShiny\"\n }\n}")
    mcmeta.close()

    logfile = open(mypath + "\\Minecraft " + mc_ver + " Randomized Textures\\log.txt", "a")
    logfile.write("Format: (File_name) is (File_image)\n\n")
    logfile.close()

    print("\nRandomizing textures\n")
    texture_randomzier = Randomizer(
        mypath + "\\assets",
        grab_files(mypath + "\\assets\\minecraft\\textures", ignored_textures),
        [],
        grab_files(mypath + "\\assets\\minecraft\\textures", ignored_textures)
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
            mypath + "\\assets",
            grab_files(mypath + "\\assets\\minecraft\\sounds", ignored_sounds),
            [],
            grab_files(mypath + "\\assets\\minecraft\\sounds", ignored_sounds)
            )
    songs_randomizer.get_all_files()
    songs_randomizer.randomized_list()
    songs_randomizer.rename_and_move(mc_ver)
    print("\nSounds have finished randomizing\n")
    zip_and_delete(mypath + "/static/zipFiles", mypath + "\\Minecraft " + mc_ver + " Randomized Textures")


# randomize("1.19", ignored_textures_default, ignored_music_default, ignored_sounds_default)
