import requests
import os
from config import ELEVENLABS_API_KEY, VOICE_ID
from utils.logger import log_event

def speak(text, emotion="neutral"):
    voice_styles = {
        "happy": "cheerful",
        "sad": "sad",
        "angry": "serious",
        "neutral": "neutral"
    }

    style = voice_styles.get(emotion, "neutral")

    url = f"https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM"
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "text": text,
        "voice_settings": {
            "stability": 0.4,
            "similarity_boost": 0.9,
            "style": style
        }
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        with open("output.mp3", "wb") as f:
            f.write(response.content)
        os.system("start output.mp3" if os.name == "nt" else "afplay output.mp3")
        log_event(f"Kiko said ({emotion}): {text}")
    else:
        print("Error in ElevenLabs API:", response.text)
