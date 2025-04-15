from services.weather_api import get_weather
from services.music_api import play_music
import webbrowser

def handle_command(text):
    text = text.lower()

    if "weather" in text:
        return get_weather()

    if "play" in text or "song" in text or "baja" in text:
        return play_music(text)

    if "open google" in text:
        webbrowser.open("https://google.com")
        return "Google khol diya."

    return None
