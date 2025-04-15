from deepface import DeepFace
import cv2

def get_emotion():
    try:
        cam = cv2.VideoCapture(0)
        ret, frame = cam.read()
        cam.release()

        if ret:
            result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
            dominant_emotion = result[0]['dominant_emotion']
            return dominant_emotion
        else:
            return "neutral"
    except:
        return "neutral"
