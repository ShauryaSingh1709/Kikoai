import pywhatkit

def play_music(query):
    try:
        song = query.replace("kiko", "").replace("play", "").replace("song", "").strip()
        pywhatkit.playonyt(song)
        return f"Chalo bajate hain: {song}"
    except:
        return "Gana nahi chala paaya."
