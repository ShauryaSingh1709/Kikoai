from datetime import datetime

def log_event(text):
    with open("kiko_log.txt", "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}] {text}\n")
