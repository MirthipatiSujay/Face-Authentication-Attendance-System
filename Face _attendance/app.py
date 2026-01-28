import cv2
import numpy as np
from attendance import mark_attendance
from anti_spoof import motion_liveness
import pickle

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("data/model.yml")


with open("data/labels.pkl", "rb") as f:
    label_map = pickle.load(f)


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        roi = gray[y:y+h, x:x+w]
        label, confidence = recognizer.predict(roi)

        if confidence < 55 and motion_liveness((x, y, w, h)):
            name = label_map[label]
            status = mark_attendance(name)
        else:
            name = "Unknown"
            status = ""

        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(frame,f"{name} {status}",(x,y-10),
                    cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)

    cv2.imshow("Attendance System", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
