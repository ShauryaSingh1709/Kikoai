import os

def get_avatar_path():
    return os.path.join("assets", "avatar", "default.gif")

def get_sound_path(name):
    return os.path.join("assets", "sounds", f"{name}.mp3")
