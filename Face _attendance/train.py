import cv2
import os
import numpy as np
import pickle

data_dir = "data/faces"
faces, labels = [], []
label_map = {}
label_id = 0

for person in sorted(os.listdir(data_dir)):
    person_dir = os.path.join(data_dir, person)
    label_map[label_id] = person

    for img in os.listdir(person_dir):
        img_path = os.path.join(person_dir, img)
        face = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        face = cv2.resize(face, (200, 200))
        faces.append(face)
        labels.append(label_id)

    label_id += 1

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.train(faces, np.array(labels))
recognizer.save("data/model.yml")

# ✅ Save label map
with open("data/labels.pkl", "wb") as f:
    pickle.dump(label_map, f)

print("Training complete and labels saved")
