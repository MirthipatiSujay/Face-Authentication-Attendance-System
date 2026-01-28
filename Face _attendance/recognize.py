import cv2

def recognize_face(gray_face, recognizer, threshold=55):
    label, confidence = recognizer.predict(gray_face)
    if confidence < threshold:
        return label, confidence
    return None, confidence
