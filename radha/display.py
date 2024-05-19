import os
import random


def change_wallpaper():
    wallpaper_path = '/home/avc/Pictures/'
    wallpapers = os.listdir(wallpaper_path)
    wallpaper = random.choice(wallpapers)
    print(wallpaper)
    command = 'gsettings set org.gnome.desktop.background picture-uri file:///'+wallpaper_path+wallpaper
    os.system(command)
    return "Wallpaper changed"

# change_wallpaper()
    