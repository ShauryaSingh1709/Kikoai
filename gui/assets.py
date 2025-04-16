import os

def get_avatar_path(name="default"):
    """
    Returns the path to the avatar image based on the given name.
    If not found, returns the path to the default avatar.
    """
    base_path = os.path.join(os.path.dirname(__file__), "avatars")
    avatar_file = f"{name}.png"
    full_path = os.path.join(base_path, avatar_file)

    if not os.path.exists(full_path):
        return os.path.join(base_path, "default.png")

    return full_path
