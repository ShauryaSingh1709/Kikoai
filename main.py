from voice.listen import listen
from voice.speak import speak
from core.brain import process_query
from gui.interface import start_gui
from services.face_emotion import get_emotion
from utils.logger import log_event

def main():
    log_event("Kiko started")
    speak("Hello Shaurya, Kiko is now active!")

    # Detect your face emotion once at start
    emotion = get_emotion()
    speak(f"Kya haal hai? Tum {emotion} lag rahe ho aj.", emotion=emotion)

    # Start GUI in background (non-blocking)
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
