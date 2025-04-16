from voice.listen import listen
from voice.speak import speak
from core.brain import process_query
from utils.logger import log_event

try:
    from gui.interface import start_gui
    from services.face_emotion import get_emotion
except ModuleNotFoundError as e:
    print("Module import error:", e)
    start_gui = None
    get_emotion = lambda: "neutral"

def main():
    log_event("Kiko started")
    speak("Hello Shaurya, Kiko is now active!")

    # Detect your face emotion once at start
    emotion = get_emotion()
    speak(f"Kya haal hai? Tum {emotion} lag rahe ho aj.", emotion=emotion)

    # Start GUI if available
    if start_gui:
        start_gui()

    while True:
        try:
            query = listen()
            if query:
                response = process_query(query)
                speak(response)
        except KeyboardInterrupt:
            speak("Bye Shaurya, milte hain phir!")
            break

if __name__ == "__main__":
    main()
