# Face Authentication Attendance System

## Overview
This project implements a face authentication based attendance system using computer vision techniques. The system registers users, recognizes faces in real time, performs basic liveness verification, and logs attendance (punch-in / punch-out).

## Features
- Face registration using webcam
- Face recognition using LBPH
- Motion-based liveness detection
- Punch-in / Punch-out attendance logging
- Fully local execution (no cloud dependencies)

## Tech Stack
- Python
- OpenCV (LBPH)
- NumPy
- Pandas

## Project Structure
face-attendance/
├── register.py
├── train.py
├── app.py
├── attendance.py
├── anti_spoof.py
├── recognize.py
├── utils.py
├── data/
│ └── faces/
├── haarcascade_frontalface_default.xml
├── requirements.txt
└── README.md


## How to Run

    ### 1. Install Dependencies
    ```bash
    pip install -r requirements.txt
    
    2. Register Face
    python register.py

    3. Train Model
    python train.py
    
    4. Run Attendance System
    python app.py

Output
Attendance records are stored in data/attendance.csv

Liveness Detection
The system uses motion-based liveness detection by analyzing face movement across consecutive frames to prevent photo spoofing.

Limitations
May fail under extreme lighting
High-quality video replays may bypass liveness detection
Not suitable for high-security applications

Deliverables
Complete working local system
Modular and documented codebase
Ready for academic or intern evaluation