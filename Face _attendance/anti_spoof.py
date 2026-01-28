import numpy as np

FACE_HISTORY = []
MAX_HISTORY = 10
MOVEMENT_THRESHOLD = 8  # pixels


def motion_liveness(face_box):
    """
    face_box: (x, y, w, h)
    """

    x, y, w, h = face_box
    cx = int(x + w / 2)
    cy = int(y + h / 2)

    FACE_HISTORY.append((cx, cy))

    if len(FACE_HISTORY) > MAX_HISTORY:
        FACE_HISTORY.pop(0)

    if len(FACE_HISTORY) < MAX_HISTORY:
        return False

    movement = 0
    for i in range(1, len(FACE_HISTORY)):
        x1, y1 = FACE_HISTORY[i - 1]
        x2, y2 = FACE_HISTORY[i]
        movement += np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    return movement > MOVEMENT_THRESHOLD

def reset_liveness():
    global FACE_HISTORY
    FACE_HISTORY = []