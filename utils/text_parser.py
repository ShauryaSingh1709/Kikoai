def extract_command(text):
    text = text.lower()
    if "weather" in text:
        return "weather"
    elif "play" in text or "song" in text:
        return "music"
    elif "time" in text:
        return "time"
    else:
        return "chat"
