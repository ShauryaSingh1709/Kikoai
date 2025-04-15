import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="hi-IN")
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        return "Mujhe samajh nahi aaya."
    except sr.RequestError:
        return "Speech service unavailable."
