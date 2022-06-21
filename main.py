import os
import shutil
from RandomizerScript import Randomizer

# This is the full ignored list, don't delete this

ignored_list = ["advancements", "container", "presets", "title", "colormap", "effect", "texts", "accessibility.png",
                "bars.png", "checkbox.png", "icons.png", "recipe_book.png", "recipe_button.png", "resource_packs.png",
                "server_selection.png", "social_interactions.png", "spectator_widgets.png", "stream_indicator.png",
                "toasts.png", "widgets.png", "world_selection.png", "rain.png", "snow.png", "end_sky.png", "clouds.png",
                "map_icons.png", "nausea.png", "powder_snow_outline.png", "pumpkinblur.png", "shadow.png",
                "spyglass_scope.png", "underwater.png", "unknown_pack.png", "unknown_server.png", "vignette.png",
                "white.png", ".gitignore", "gpu_warnlist.json", "regional_compliancies.json", "pack.png"]

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


def randomize(mc_ver, ignored):

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

    texture_randomzier = Randomizer(
        mypath + "\\assets",
        grab_files(mypath + "\\assets", ignored),
        [],
        grab_files(mypath + "\\assets", ignored)
        )

    texture_randomzier.get_all_files()
    texture_randomzier.randomized_list()
    texture_randomzier.rename_and_move(mc_ver)


# randomize("1.19", ignored_list)
