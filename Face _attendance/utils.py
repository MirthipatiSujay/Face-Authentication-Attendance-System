import os

def load_label_map(data_dir="data/faces"):
    label_map = {}
    label_id = 0

    for name in sorted(os.listdir(data_dir)):
        label_map[label_id] = name
        label_id += 1

    return label_map
